#include <stddef.h>
#include "lists.h"
/**
 * is_palindrome- checks if a singly linked list is a palindrome.
 * @head: head
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *h = *head, *temp = *head;

	if (*head == NULL)
		return (1);
	while (h != NULL)
	{
		if (temp->n != h->n)
			return (0);
		temp = temp->next;
		h = h->next;
	}
	return (1);
}
