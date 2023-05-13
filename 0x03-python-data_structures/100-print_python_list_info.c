#include "Python.h"
#include <stdlib.h>

/**
 * print_python_list_info - prints information about a python list object
 * @p: pointer to generic PyObject which is of PyListObject type
 *
 * Return: always void.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *py_list = NULL;
	ssize_t size = 0, i = 0;

	list_len = PyList_Size(p);
	py_list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", (signed long)(py_list->allocated));
	while (i < size)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(py_list->ob_item[i])->tp_name);
		i++;
	}
}
