def worker_exit(server, worker) -> None: ...
def post_fork(server, worker) -> None: ...
def pre_fork(server, worker) -> None: ...
def pre_exec(server) -> None: ...
def when_ready(server) -> None: ...
def worker_int(worker) -> None: ...
def worker_abort(worker) -> None: ...
def post_worker_init(worker) -> None: ...
