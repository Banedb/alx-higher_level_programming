#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 *
 * Return: 0 - no cycle || 1 - cycle found
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	if (list == NULL || list->next == NULL)
		return (0); /* single node or empty list == no cycle */
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1); /* Cycle detected */
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0); /* No cycle found */
}
