#include "lists.h"

/**
 * insert_node - insert number in sorted linked list
 * @head: head of linked list
 * @number: number to insert
 * Return: pointer to the new node, NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	current = *head;
	while (current->next && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
