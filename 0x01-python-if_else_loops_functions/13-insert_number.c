#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - it will insert a number in ordered linked list
 * @head: the double pointer to the linked list
 * @number: the number to be inserted in the new node
 * Return: NULL or the address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node = NULL;
	listint_t *tmp = NULL;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new_node->next = *head;
		return (*head = new_node);
	}
	else
	{
		while (current && current->n < number)
		{
			tmp = current;
			current = current->next;
		}
		tmp->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
