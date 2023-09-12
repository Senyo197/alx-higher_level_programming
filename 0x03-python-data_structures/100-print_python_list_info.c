#include <Python.h>

/**
 * print_python_list_info - Prints basic information about Python lists
 * @p: A PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	if (!PyList_Check(p))
	{
		PyErr_SetString(PyExc_TypeError, "Object is not a list");
		return;
	}

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		if (obj != NULL)
		{
			printf("%s\n", Py_TYPE(obj)->tp_name);
		}
		else
		{
			PyErr_Print();
		}
	}
}

