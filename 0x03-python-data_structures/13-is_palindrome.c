#include "lists.h"
/**
 * is_palindrome - checks if a listint_t list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 1 if palindrome || 0 if not
 */
int is_palindrome(listint_t **head)
{
	int i, num = 0;
	listint_t *current, *copy;

	if (!(head))
		return (1);
	for (current = *head; current; current = current->next)
		num++;
	for (current = *head; current; current = current->next)
	{
		for (i = 1, copy = *head; i < num; copy = copy->next, i++)
			;
		if (current->n != copy->n)
			return (0);
		num--;
	}
	return (1);
}
