#include "lists.h"

/**
  *reverse - To reverse a linked list
  *@head: The start of the list
  *Return: The reversed list
  */
listint_t *reverse(listint_t *head)
{
	listint_t *current = head;
	listint_t *previous = NULL;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	return (previous);
}


/**
  *find_middle - Find the middle of a linked list
  *@head: The start of the list
  *Return: The start of the middle half
  */
listint_t *find_middle(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	return (slow);
}


/**
  *is_palindrome - Detects if list is a palindrome
  *@head: The start of the list
  *Return: list
  */
int is_palindrome(listint_t **head)
{
	listint_t *middle = find_middle(*head);
	listint_t *reverse_half = reverse(middle);
	listint_t *current = *head;

	while (reverse_half != NULL)
	{
		if (current->n != reverse_half->n)
			return (0);

		current = current->next;
		reverse_half = reverse_half->next;
	}

	reverse(middle);
	return (1);
}
