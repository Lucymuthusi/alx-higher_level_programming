#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head) {
    listint_t *slow, *fast, *prev, *curr, *next;

    // Handle empty list (considered a palindrome)
    if (!*head) {
        return 1;
    }

    // Find the middle node using slow and fast pointers
    slow = *head;
    fast = *head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Reverse the second half of the list
    prev = NULL;
    curr = slow;
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    // Compare nodes from head and reversed half
    slow = *head;
    while (slow && prev) {
        if (slow->n != prev->n) {
            return 0;
        }
        slow = slow->next;
        prev = prev->next;
    }

    // Restore the original list (optional)
    prev = NULL;
    curr = slow;
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    return 1;
}
