#include "lists.h"

/**
  *insert_node - Insert a number into a sorted linked list
  *@head: A pointer of pointer to the start of the linked list
  *@number: The number to be inserted
  *Return: The address of the new node, or NULL if it failed
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *current, *previous;

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	current = *head;
	previous = NULL;

	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	if (previous == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		previous->next = new;
		new->next = current;
	}

	return (new);
}
