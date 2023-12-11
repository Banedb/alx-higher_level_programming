#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Print list info about Python
 * @p: Pyobject pointer
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t count;
	Py_ssize_t length = PyList_Size(p);
	PyListObject *plobj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %ld\n", plobj->allocated);

	for (count = 0; count < length; count++)
	{
		printf("Element %ld: %s\n", count,
		       Py_TYPE(plobj->ob_item[count])->tp_name);
	}
}
