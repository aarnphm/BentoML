import os
from typing import List

import easyocr
import imageio
import numpy as np

from bentoml.easyocr import EasyOCRModel

from ..._internal.bento_services.easyocr import predict_image

TEST_RESULT: List[str] = ['西', '愚园路', '东', '315', '309', 'W', 'Yuyuan Rd。', 'E']
IMAGE_PATH: str = './tests/integration/frameworks/_static/chinese.jpg'


def test_easyocr_save_load(tmpdir):
    language_list = ['ch_sim', 'en']
    recog_network = "zh_sim_g2"

    model = easyocr.Reader(
        lang_list=language_list,
        gpu=False,
        download_enabled=True,
        recog_network=recog_network,
    )
    assert [x[1] for x in model.readtext(IMAGE_PATH)] == TEST_RESULT

    EasyOCRModel(
        model,
        recog_network=recog_network,
        language_list=language_list,
        name='chinese_small',
    ).save(tmpdir)
    assert os.path.exists(EasyOCRModel.get_path(tmpdir, ".json"))

    easyocr_loaded: easyocr.Reader = EasyOCRModel.load(tmpdir)

    image = imageio.imread(IMAGE_PATH)
    assert predict_image(easyocr_loaded, np.array(image)) == TEST_RESULT
