
def measure(fn,*args,repeat=1,out:list=None):
	# Other option are: process_time , perf_counter
	from time import perf_counter as counter
	t = counter()

	for i in range(repeat): 
		result = fn(*args)
		if hasattr(out,"append"):
			out.append(result)

	elapsed = counter() - t
	print(f"Took {elapsed:.4f}s for {str(fn)} to run {repeat} times")
	return elapsed


def measure_all(fns:list,*args,repeat=1):
	# Other option are: process_time , perf_counter
	from time import process_time as counter
	for fn in fns:
		measure(fn, *args,repeat=repeat)