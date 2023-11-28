#include "lists.h"
/**
 * insert_node - adds a new node to sorted listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (current == NULL) /* empty node */
	{
		new->n = number;
		new->next = NULL;
		*head = new;
		return (new);
	}
	else if (current->n > number) /* first node */
	{
		new->n = number;
		new->next = current;
		*head = new;
		return (new);
	}
	else
	{
		for (; current;)
		{
			if (current->n <= number && (current->next == NULL ||
						    current->next->n > number))
			{
				new->n = number;
				new->next = current->next;
				current->next = new;
				return (new);
			}
			current = current->next;
		}
	}
	return (NULL);
}
