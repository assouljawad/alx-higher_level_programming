#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - it's shows info about python lists
 * @p: object
 *
 * Return: 0
 */
void print_python_list_info(PyObject *p)
{
	long int ls_size, w, i;

	i = 0;
	PyObject *obj;

	ls_size = PyList_Size(p);
	w = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", ls_size);
	printf("[*] Allocated = %ld\n", w);
	while (i < ls_size)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
