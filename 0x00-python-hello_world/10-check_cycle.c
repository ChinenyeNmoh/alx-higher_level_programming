#include "lists.h"
/**
 * check_cycle - checks if a linked list is circular or not
 *
 * @list: linked list to check
 *
 * Return: 1 (linked list is circular) 0 (no loop detected)
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = NULL, *slow = NULL;

	list = fast = slow;
	if (!list || fast || slow)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
