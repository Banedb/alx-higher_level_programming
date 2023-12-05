#include "lists.h"
/**
 * is_palindrome - checks if a listint_t list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 1 if palindrome || 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *current;
	listint_t *prev = NULL, *next = NULL, *second_half_start = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1); /* empty list or a list with a single element */
	while (fast && fast->next)
	{ /* Find the midpoint of the linked list */
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	/* Adjust pointers for odd/even number of elements */
	if (fast != NULL) /* If num elements is odd, move slow one step ahead */
		second_half_start = slow->next;
	else /* If the num elements is even, slow is at midpoint */
		second_half_start = slow;
	/* Reverse the second half of the linked list */
	current = second_half_start;
	prev = NULL;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	second_half_start = prev; /* New head of the reversed second half */
	while (second_half_start != NULL)
	{ /* check palindrome */
		if ((*head)->n != second_half_start->n)
			return (0); /* Not a palindrome */
		*head = (*head)->next;
		second_half_start = second_half_start->next;
	}
	return (1); /* It's a palindrome */
}
