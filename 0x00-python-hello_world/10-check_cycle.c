#include "lists.h"

/**
  *check_cycle - Checks if singly linked list has a cycle in it
  *@list: Linked list to be checked
  *Return: 0 if no list, 1 otherwise
  */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
