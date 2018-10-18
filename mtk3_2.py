import itertools
import hashlib
from threading import Thread
import time
import sys 

lenth = 8
threads = 8
sha1 = '67ae1a64661ac8b4494666f58c4822408dd0a3e4'
ch_group = ['QW%(=I*N', 'QW%(=I*n', 'QW%(=I+N', 'QW%(=I+n', 'QW%(=i*N', 'QW%(=i*n', 'QW%(=i+N', 'QW%(=i+n', 'QW%(0I*N', 'QW%(0I*n', 'QW%(0I+N', 'QW%(0I+n', 'QW%(0i*N', 'QW%(0i*n', 'QW%(0i+N', 'QW%(0i+n', 'QW%8=I*N', 'QW%8=I*n', 'QW%8=I+N', 'QW%8=I+n', 'QW%8=i*N', 'QW%8=i*n', 'QW%8=i+N', 'QW%8=i+n', 'QW%80I*N', 'QW%80I*n', 'QW%80I+N', 'QW%80I+n', 'QW%80i*N', 'QW%80i*n', 'QW%80i+N', 'QW%80i+n', 'QW5(=I*N', 'QW5(=I*n', 'QW5(=I+N', 'QW5(=I+n', 'QW5(=i*N', 'QW5(=i*n', 'QW5(=i+N', 'QW5(=i+n', 'QW5(0I*N', 'QW5(0I*n', 'QW5(0I+N', 'QW5(0I+n', 'QW5(0i*N', 'QW5(0i*n', 'QW5(0i+N', 'QW5(0i+n', 'QW58=I*N', 'QW58=I*n', 'QW58=I+N', 'QW58=I+n', 'QW58=i*N', 'QW58=i*n', 'QW58=i+N', 'QW58=i+n', 'QW580I*N', 'QW580I*n', 'QW580I+N', 'QW580I+n', 'QW580i*N', 'QW580i*n', 'QW580i+N', 'QW580i+n', 'Qw%(=I*N', 'Qw%(=I*n', 'Qw%(=I+N', 'Qw%(=I+n', 'Qw%(=i*N', 'Qw%(=i*n', 'Qw%(=i+N', 'Qw%(=i+n', 'Qw%(0I*N', 'Qw%(0I*n', 'Qw%(0I+N', 'Qw%(0I+n', 'Qw%(0i*N', 'Qw%(0i*n', 'Qw%(0i+N', 'Qw%(0i+n', 'Qw%8=I*N', 'Qw%8=I*n', 'Qw%8=I+N', 'Qw%8=I+n', 'Qw%8=i*N', 'Qw%8=i*n', 'Qw%8=i+N', 'Qw%8=i+n', 'Qw%80I*N', 'Qw%80I*n', 'Qw%80I+N', 'Qw%80I+n', 'Qw%80i*N', 'Qw%80i*n', 'Qw%80i+N', 'Qw%80i+n', 'Qw5(=I*N', 'Qw5(=I*n', 'Qw5(=I+N', 'Qw5(=I+n', 'Qw5(=i*N', 'Qw5(=i*n', 'Qw5(=i+N', 'Qw5(=i+n', 'Qw5(0I*N', 'Qw5(0I*n', 'Qw5(0I+N', 'Qw5(0I+n', 'Qw5(0i*N', 'Qw5(0i*n', 'Qw5(0i+N', 'Qw5(0i+n', 'Qw58=I*N', 'Qw58=I*n', 'Qw58=I+N', 'Qw58=I+n', 'Qw58=i*N', 'Qw58=i*n', 'Qw58=i+N', 'Qw58=i+n', 'Qw580I*N', 'Qw580I*n', 'Qw580I+N', 'Qw580I+n', 'Qw580i*N', 'Qw580i*n', 'Qw580i+N', 'Qw580i+n', 'qW%(=I*N', 'qW%(=I*n', 'qW%(=I+N', 'qW%(=I+n', 'qW%(=i*N', 'qW%(=i*n', 'qW%(=i+N', 'qW%(=i+n', 'qW%(0I*N', 'qW%(0I*n', 'qW%(0I+N', 'qW%(0I+n', 'qW%(0i*N', 'qW%(0i*n', 'qW%(0i+N', 'qW%(0i+n', 'qW%8=I*N', 'qW%8=I*n', 'qW%8=I+N', 'qW%8=I+n', 'qW%8=i*N', 'qW%8=i*n', 'qW%8=i+N', 'qW%8=i+n', 'qW%80I*N', 'qW%80I*n', 'qW%80I+N', 'qW%80I+n', 'qW%80i*N', 'qW%80i*n', 'qW%80i+N', 'qW%80i+n', 'qW5(=I*N', 'qW5(=I*n', 'qW5(=I+N', 'qW5(=I+n', 'qW5(=i*N', 'qW5(=i*n', 'qW5(=i+N', 'qW5(=i+n', 'qW5(0I*N', 'qW5(0I*n', 'qW5(0I+N', 'qW5(0I+n', 'qW5(0i*N', 'qW5(0i*n', 'qW5(0i+N', 'qW5(0i+n', 'qW58=I*N', 'qW58=I*n', 'qW58=I+N', 'qW58=I+n', 'qW58=i*N', 'qW58=i*n', 'qW58=i+N', 'qW58=i+n', 'qW580I*N', 'qW580I*n', 'qW580I+N', 'qW580I+n', 'qW580i*N', 'qW580i*n', 'qW580i+N', 'qW580i+n', 'qw%(=I*N', 'qw%(=I*n', 'qw%(=I+N', 'qw%(=I+n', 'qw%(=i*N', 'qw%(=i*n', 'qw%(=i+N', 'qw%(=i+n', 'qw%(0I*N', 'qw%(0I*n', 'qw%(0I+N', 'qw%(0I+n', 'qw%(0i*N', 'qw%(0i*n', 'qw%(0i+N', 'qw%(0i+n', 'qw%8=I*N', 'qw%8=I*n', 'qw%8=I+N', 'qw%8=I+n', 'qw%8=i*N', 'qw%8=i*n', 'qw%8=i+N', 'qw%8=i+n', 'qw%80I*N', 'qw%80I*n', 'qw%80I+N', 'qw%80I+n', 'qw%80i*N', 'qw%80i*n', 'qw%80i+N', 'qw%80i+n', 'qw5(=I*N', 'qw5(=I*n', 'qw5(=I+N', 'qw5(=I+n', 'qw5(=i*N', 'qw5(=i*n', 'qw5(=i+N', 'qw5(=i+n', 'qw5(0I*N', 'qw5(0I*n', 'qw5(0I+N', 'qw5(0I+n', 'qw5(0i*N', 'qw5(0i*n', 'qw5(0i+N', 'qw5(0i+n', 'qw58=I*N', 'qw58=I*n', 'qw58=I+N', 'qw58=I+n', 'qw58=i*N', 'qw58=i*n', 'qw58=i+N', 'qw58=i+n', 'qw580I*N', 'qw580I*n', 'qw580I+N', 'qw580I+n', 'qw580i*N', 'qw580i*n', 'qw580i+N', 'qw580i+n']
group_num = len(ch_group)

def trackOneGroup(group_id,lenth,stime):
	for i in itertools.permutations(ch_group[group_id],lenth):
		h = hashlib.sha1(''.join(i)).hexdigest()
		if(h == sha1):
			print('Answer:'+''.join(i))
			print('Cost:'+str(time.time()-stime)+'s')

def trackThread(thread_id,lenth,stime):
	num_per_thread = group_num//threads	
	for i in range(num_per_thread):
		trackOneGroup(thread_id*num_per_thread+i,lenth,stime)

def main():
	thread_pool = []
	stime = time.time()
	for i in range(threads):
		t = Thread(target=trackThread,args=(i,lenth,stime,))
		thread_pool.append(t)
	for mythread in thread_pool:
		mythread.start()

if __name__ == '__main__':
	main()
