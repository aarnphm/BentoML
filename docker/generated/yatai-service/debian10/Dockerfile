# syntax = docker/dockerfile:1.2
#
# ===========================================
#
# THIS IS A GENERATED DOCKERFILE DO NOT EDIT.
#
# ===========================================


FROM debian:buster-slim

# setup ENV and ARG
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ARG PYTHON_VERSION

ENV PATH /opt/conda/bin:$PATH

ENV DEBIAN_FRONTEND noninteractive

# needed for string substitution
SHELL ["/bin/bash","-exo", "pipefail", "-c"]

RUN apt-get update && \
    apt-get install -q -y --no-install-recommends \
    ca-certificates curl wget git gnupg build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    apt-get clean && apt-get autoremove -y && \
    apt-get purge -y wget

RUN /opt/conda/bin/conda install -y python=$PYTHON_VERSION pip && \
    /opt/conda/bin/conda clean -afy

# YataiService GRPC port
EXPOSE 50051

# YataiService Web UI port
EXPOSE 3000

# Install Node, required by the Web UI Server
# https://github.com/nodejs/docker-node/blob/main/16/buster-slim/Dockerfile
ENV NODE_VERSION 16.3.0

# https://github.com/docker-library/faq#openpgp--gnupg-keys-and-verification
RUN ARCH='' \
    && dpkgArch="$(dpkg --print-architecture)" \
    && case "${dpkgArch##*-}" in \
      amd64) ARCH='x64';; \
      ppc64el) ARCH='ppc64le';; \
      s390x) ARCH='s390x';; \
      arm64) ARCH='arm64';; \
      armhf) ARCH='armv7l';; \
      i386) ARCH='x86';; \
      *) echo "unsupported architecture"; exit 1 ;; \
    esac \
    && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
    && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
    && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
    && apt-mark auto '.*' > /dev/null \
    && apt-mark manual git build-essential \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && ln -s /usr/local/bin/node /usr/local/bin/nodejs \
    # smoke tests
    && node --version \
    && npm --version

RUN apt-get update && apt-get install -q -y --no-install-recommends libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY tools/bashrc /etc/bash.bashrc
RUN chmod a+r /etc/bash.bashrc