#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - will check if the linked list has cycle in it
 * @list: the linked list
 * Return: n int
 */
int check_cycle(listint_t *list)
{
	listint_t *lists = list;
	listint_t *auxil = lists;

	while (lists && auxil && lists->next)
	{
		auxil = auxil->next;
		lists = lists->next->next;
		if (auxil == lists)
			return (1);
	}
	return (0);
}
