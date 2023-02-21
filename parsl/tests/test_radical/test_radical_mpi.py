import parsl


@parsl.python_app
def test_mpi(comm):
    import time
    print('hello %d/%d' % (comm.rank, comm.size))
    time.sleep(0.1)
    return True


apps = []


def test_mpi_radical(n=10):
    for _ in range(n):
        fut = test_mpi(None)
        apps.append(fut)


[app.result() for app in apps]


if __name__ == "__main__":
    test_mpi_radical()
