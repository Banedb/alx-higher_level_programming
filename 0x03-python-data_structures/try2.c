#include "lists.h"
/**
 * is_palindrome - checks if a listint_t list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 1 if palindrome || 0 if not
 */
int is_palindrome(listint_t **head)
{
	int i, j, num = 0;
	listint_t *check, *copy;

	if (!(head))
		return (1);
	for (check = *head; check; check = check->next)
		num++;
	num--;
	j = num;
	for (check = *head; check; check = check->next)
	{
		for (i = j - num, copy = check; i < num; copy = copy->next, i++)
			;
		if (check->n != copy->n)
			return (0);
		num--;
	}
	return (1);
}
