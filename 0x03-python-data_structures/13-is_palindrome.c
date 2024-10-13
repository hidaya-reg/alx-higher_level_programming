#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to list to be freed
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first, *second;
	int i, j, length = 0;

	if (*head == NULL)
		return (1);

	first = *head;

	while (first->next != NULL)
	{
		first = first->next;
		length++;
	}
	length++;

	second = *head;
	first = *head;
	for (i = 0; i < (length / 2) - 1; i++)
	{
		second = second->next;
		first = first->next;
	}
	if (length % 2 == 0)
		second = second->next;
	else
		second = second->next->next;
	while (i > 0)
	{
		if (first->n != second->n)
		{
			return (0);
		}
		first = *head;
		second = second->next;
		i--;
		for (j = 0; j < i; j++)
			first = first->next;
	}
	return (1);
}
