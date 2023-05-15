#include "lists.h"
#include <stdio.h>

void reverse(listint_t **head);
int is_palindrome(listint_t **head);
/**
 * reverse - reverses a linked list
 * @head: double pointer to head of linked list so we can modify it
 *
 * Return: always void, modifies head itself.
 */
void reverse(listint_t **head)
{
	listint_t *prev, *current, *nextnode;

	if (head == NULL)
		return;
	prev = NULL;
	current = nextnode = *head;
	while (nextnode != NULL)
	{
		nextnode = nextnode->next;
		current->next = prev;
		prev = current;
		current = nextnode;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 0 (not palindrome) 1 (is palindrome)
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
