#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * print_python_list_info - prints information about a python list object
 * @p: pointer to generic PyObject which is of PyListObject type
 *
 * Return: always void.
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i = 0;
	const char *ele_type;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	while (i < size)
	{
		ele_type = Py_TYPE(obj->ob_item[i])->tp_name
		printf("Element %i: %s\n", i, ele_type);
		i++;
	}
}
