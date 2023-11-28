#include "lists.h"
/**
 * insert_node - adds a new node to sorted listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = current;
	/* empty or first node */
	if (current == NULL || current->n > number)
	{
		*head = new;
		return (new);
	}
	else /* centre or end */
	{
		for (; current; current = current->next)
		{
			if (current->n <= number && (current->next == NULL ||
						    current->next->n > number))
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
		}
	}
	return (NULL);
}
