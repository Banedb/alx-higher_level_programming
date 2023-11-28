#include "shell.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (!(current->next))
	{
		new->n = number;
		new->next = NULL;
		*head = new;
		return (new);
	}
	else
	{
		for (; current->n;)
		{
			if ((current->n < number) && current->next > number)
			{
				new->n = number;
				new->next = current->next;
				current->next = new;
			}
			current->next = current->next->next;
		}
	}
}
