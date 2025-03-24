#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - prints info about python lists
 * @p: address of pyobject struct
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size, len;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	len = size > 10 ? 10 : size + 1;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes: ", len);
	for (i = 0; i < len; i++)
		printf("%02x%s",
		       (unsigned char)str[i], i == len - 1 ? "" : " ");
	printf("\n");
}

/**
 * print_python_list - prints info about python lists
 * @p: address of pyobject struct
 */

void print_python_list(PyObject *p)
{
	PyObject *item, *item_type;
	Py_ssize_t i, alloc, size = PyList_Size(p);
	PyTypeObject *type;

	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		item_type = PyObject_Type(item);
		if (item_type)
		{
			type = (PyTypeObject *)item_type;
			printf("Element %ld: %s\n", i, type->tp_name);
			if (strcmp(type->tp_name, "bytes") == 0)
				print_python_bytes(item);
			Py_DECREF(item_type);
		}
	}
}
