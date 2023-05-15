#include "lists.h"
#include <stdio.h>
listint_t *findmiddle(listint_t *head);
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
 * findmiddle - finds the middle of a linked list
 * @head: pointer to head of linked list so we can modify it
 *
 * Return: middle node
 */
listint_t *findmiddle(listint_t *head)
{
	if (head == NULL)
		return (NULL);
	listint_t *fast, *slow;

	fast = head;
	slow = head;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	return (slow);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 0 (not palindrome) 1 (is palindrome)
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *mid = findmiddle(*head);
	listint_t *tempHead = *head;

	reverse(&mid);
	while (mid != NULL)
	{
		if (tempHead->n != mid->n)
			return (0);
		tempHead = tempHead->next;
		mid = mid->next;
	}
	return (1);
}
