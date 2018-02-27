#include <stdio.h>
#include <windows.h>

void main()
{
	LARGE_INTEGER ticksPerSecond;
	LARGE_INTEGER start_ticks, end_ticks, diff_ticks; 

	QueryPerformanceCounter(&start_ticks);

	/*
	~~
	~~~
	Algorithm
	~~~
	~~
	*/

	QueryPerformanceCounter(&end_ticks);
	QueryPerformanceFrequency(&ticksPerSecond);
	diff_ticks.QuadPart = end_ticks.QuadPart- start_ticks.QuadPart;

 	printf("Elapsed CPU time:   %.12f  sec\n\n",
		((double)diff_ticks.QuadPart/(double)ticksPerSecond.QuadPart));
}
