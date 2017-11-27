/*
 * File: hw11.c
 * Project: CS 125 Assignment 11
 * Purpose: Create structs to define a polygon and its perimeter
 * Author: Joshua Paul Rodriguez
 * Version: 1.0 November 7, 2017
 *          1.1 November 8, 2017 added variable polygon support
 */
#include <stdio.h> /* for printf */
#include <stdlib.h> /* for RAND_MAX */
#include <math.h> /* for sqrt() */
#define MAX_LEN 64 /* max array length */

/* a pair of doubles */
typedef struct {
    double x;
    double y;
} Point;

/* a triple of points in an array */
typedef struct {
    Point vertex[MAX_LEN];
    int numOfVertex;
} Polygon;

/* prompts and reprompts for a number */
int enterNumOfVertex(void);
/* prompts and reprompts for a coord */
Point enterPoint(void);
/* calculates and returns a coord of the perimeter of a given polygon */
double perimeter(const Polygon* pol);
/* calculates and returns the distance between 2 given points */
double distanceBetweenPoints(const Point* p1, const Point* p2);
/* prints the verticies and verbaige to console */
void printVertices(const Polygon* pol);

int main(void) {
    int i;
    Polygon poly;
    double perim;

    poly.numOfVertex = enterNumOfVertex();
    /* for each vertex of the polygon, store a point */
    for (i = 0; i < poly.numOfVertex; i++) {
        poly.vertex[i] = enterPoint();
    }
    perim = perimeter(&poly);
    printVertices(&poly);
    printf("The perimeter is %.2f\n", perim);
    return 0;
}

/* prompts and reprompts for a valid number */
int enterNumOfVertex(void) {
    int number;
    printf("Enter the number of vertices: ");
    /* runs the loop as long as the user has not entered a valid num */
    /* then reprompts the user */
    while (scanf("%d", &number) != 1) {
        scanf("%*[^\n]");
        printf("Integer could not be read. Try again.\n");
        printf("Enter the number of vertices: ");
    }
    return number;
}

/* prompts and reprompts for a valid coord */
Point enterPoint(void) {
    Point punkt;
    printf("Enter the x and y coordinates separated by a comma: ");
    /* runs the loop as long as the user has not entered valid nums */
    /* then reprompts the user */
    while (scanf("%lf,%lf", &punkt.x, &punkt.y) != 2) {
        scanf("%*[^\n]");
        printf("Coordinates could not be read. Try again.\n");
        printf("Enter the x and y coordinates separated by a comma: ");
    }
    return punkt;
}

/* calculates and returns a coord of the perimeter of a given polygon */
double perimeter(const Polygon* pol) {
    double perimeter = 0.0;
    int i;
    /* iterates though the different edges of the polygon except the last */
    /* assuming that 2 consecuative points are connected by an edge */
    for (i = 0; i < pol->numOfVertex - 1; i++)
        perimeter += distanceBetweenPoints(&pol->vertex[i], &pol->vertex[i+1]);
    /* last edge has to go from the last point to the first point */
    perimeter += distanceBetweenPoints(&pol->vertex[i], &pol->vertex[0]);
    return perimeter; 
}

/* calculates and returns the distance between 2 given points */
double distanceBetweenPoints(const Point* p1, const Point* p2) {
    double xDiff = p1->x - p2->x;
    double yDiff = p1->y - p2->y;
    double distance = sqrt((xDiff * xDiff) + (yDiff * yDiff));
    return distance;
}

/* prints the verticies and verbaige to console */
void printVertices(const Polygon* pol) {
    int i;
    printf("The point coordinates are: ");
    /* iterates though the vertecies */
    for (i = 0; i < pol->numOfVertex - 1; i++)
            printf("[%.2f,%.2f],", pol->vertex[i].x, pol->vertex[i].y);
    /* prints values and newline for the last vertex */
    printf("[%.2f,%.2f]\n", pol->vertex[i].x, pol->vertex[i].y);
}