#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * is_palindrome- will check if a singly linked list is a palindrome.
 * @head: double head pointer
 * Return: 0 if it's not a palindrome, 1 if it's a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int values[9999];
	int j = 0, a = 0;

	if ((!*head) || (!head))
	{
		return (1);
	}
	node = *head;
	if (!node->next)
	{
		return (1);
	}
	while (node)
	{
		values[j] = node->n;
		node = node->next;
		j++;
	}
	j--;
	while (j >= 0 && a <= j)
	{
		if (values[j] != values[a])
		{
			return (0);
		}
		j--;
		a++;
	}
	return (1);
}
