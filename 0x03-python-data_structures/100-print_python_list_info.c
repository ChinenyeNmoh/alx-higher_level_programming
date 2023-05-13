#include <object.h>
#include <listobject.h>
#include <Python.h>
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
