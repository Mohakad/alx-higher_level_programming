#include "lists.h"
/**
 *check_cycle- hecks if a singly linked list has a cycle in it.
 *Return: 0 if there is no cycle, 1 if there is a cycle
 *@list: list
 */
int check_cycle(listint_t *list)
{
	listint_t *onenext = list;

	listint_t *twonext = list;

	if (!list)
		return (0);
	while (onenext && twonext && twonext->next)
	{
		onenext = onenext->next;
		twonext = twonext->next->next;
		if (onenext == twonext) /*If list has a loop they will definitely meet*/
			return (1);
	}
	return (0);
}
