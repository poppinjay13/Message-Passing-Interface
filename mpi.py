from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
num_p = comm.Get_size()


if rank != 0:
    comm.send("Hello From " + str(rank), dest=0)
else:
    for pid in range(1, num_p):
        print("Message: ", comm.recv(source=pid))
