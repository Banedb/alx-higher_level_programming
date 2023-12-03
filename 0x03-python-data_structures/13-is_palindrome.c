#include "lists.h"
/**
 * is_palindrome - checks if a listint_t list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 1 if palindrome || 0 if not
 */
int is_palindrome(listint_t **head)
{
	int i, j, *new[1024];
	listint_t *check;

	if (!(head))
		return (1);
	for (check = *head, i = 0; check; check = check->next, i++)
		;
	for (check = *head, j = 0; check; check = check->next, j++)
		new[j] = check->n;
	for (check = *head, i--; check; check = check->next)
	{
		if (check->n != new[i])
			return (0);
		i--;
	}
	return (1);
}
