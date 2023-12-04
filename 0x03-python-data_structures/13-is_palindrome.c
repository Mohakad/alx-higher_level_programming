#include <stddef.h>
#include "lists.h"
/**
 * is_palindrome- checks if a singly linked list is a palindrome.
 * @head: head
 * Return: 0 or 1
*/
int is_palindrome(listint_t **head)
{
    listint_t *h = *head, *temp = NULL, *t2 = NULL;

    if (h->next == NULL || *head == NULL)
        return (1);
    while (h != NULL)
    {
        add_nodeint_end(&temp, h->n);
        h = h->next;
    }
    t2 = temp;
    while (*head != NULL)
    {
        if (t2->n != (*head)->n)
        {
            free_listint(temp);
            return (0);
        }
        t2 = t2->next;
        *head = (*head)->next;
    }
    free_listint(temp);
    return (1);
}