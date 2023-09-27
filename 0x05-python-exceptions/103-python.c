#include <Python.h>
#include <stdio.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
	PyObject *item;
	Py_ssize_t size, i;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < 9)
			printf(" ");
	}
	printf("\n");
}
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}
	printf("[.] float object info\n");
	printf("  value: %f\n", PyFloat_AsDouble(p));
}

