/**
 * Author: GabieSE
 * Filename: 13-is_palindrome.c
 */
#include "lists.h"
#include <stddef.h>
/**
 * @*reverse_listint -It reverses a linked list in place
 * @head: It is a pointer to a pointer.
 * Return: The new head of the reversed list
 */
listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - It checks if it is palindrome.
 * reverse_listint - a func that reverses a linked list in place
 * @head: A head pointer
 * Return: If the linked list is not a palindrome - 0.
 * If the linked list is a palindrome - 1.
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}
	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;
	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);
	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;
	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);
	return (1);
}
