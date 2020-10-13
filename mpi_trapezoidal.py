from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
num_p = comm.Get_size()

if rank == 1:
    # start first process
    comm.send(2/2, dest=0)
elif rank == 2:
    # start second process
    comm.send(4 + 5, dest=0)
elif rank == 3:
    # start third process
    comm.send(2 * (6 + 6 + 4 + 4), dest=0)
elif rank == 0:
    # get process results and sum to get area
    p1_res = int(comm.recv(source=1))
    p2_res = int(comm.recv(source=2))
    p3_res = int(comm.recv(source=3))
    area = p1_res + p2_res + p3_res
    print("The area under the curve is "+str(area))
