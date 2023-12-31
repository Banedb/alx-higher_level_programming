#include "lists.h"
/**
 * is_palindrome - checks if a listint_t list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 1 if palindrome || 0 if not
 */
int is_palindrome(listint_t **head)
{
	int i, j, *new;
	listint_t *check;

	if (!(head))
		return (1);
	for (check = *head, i = 0; check; check = check->next, i++)
		;
	new = malloc(sizeof(int) * i);
	for (check = *head, j = 0; check; check = check->next, j++)
		new[j] = check->n;
	for (check = *head, i--; check; check = check->next)
	{
		if (check->n != new[i])
		{
			free(new);
			return (0);
		}
		i--;
	}
	free(new);
	return (1);
}
