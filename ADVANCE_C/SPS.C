#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() 
{
    char name[50];
    int userChoice, computerChoice;
    int userScore = 0, computerScore = 0;
    int roundNumber = 1;

    srand(time(0)); 

    printf("=== WELCOME TO THE DANGAL (Stone, Paper, Scissors) ===\n");
    printf("Enter your name, Champion: ");
    scanf("%s", name);

    printf("\nGet ready %s! First to get 3 points WINS the final match! [🏆]\n\n", name);

    
    while (userScore < 3 && computerScore < 3) 
    {
        printf("--- ROUND %d ---\n", roundNumber);
        printf("1. Stone\n");
        printf("2. Paper\n");
        printf("3. Scissors\n");
        printf("Choose your weapon (1, 2, or 3): ");
        scanf("%d", &userChoice);

        
        computerChoice = (rand() % 3) + 1; 

        
        if (computerChoice == 1) printf("Computer chose: Stone\n");
        else if (computerChoice == 2) printf("Computer chose: Paper\n");
        else printf("Computer chose: Scissors\n");

        
        if (userChoice == computerChoice) 
        {
            printf("It's a TIE for this round! [Match Draw]\n");
        } 
        
        else if ((userChoice == 1 && computerChoice == 3) || 
                 (userChoice == 2 && computerChoice == 1) || 
                 (userChoice == 3 && computerChoice == 2)) 
        {
            userScore++; 
            printf("Point goes to %s! [SUCCESS]\n", name);
        } 
        else 
        {
            computerScore++; 
            printf("Point goes to Computer! [COMPUTER SCORED]\n");
        }


        printf("SCOREBOARD -> %s: %d | Computer: %d\n\n", name, userScore, computerScore);
        roundNumber++;
    }

    
    printf("=========================================\n");
    if (userScore == 3) 
    {
        printf("CONGRATULATIONS %s! You won the DANGAL match! [CHAMPION]\n", name);
    } 
    else 
    {
        printf("GAME OVER! Computer won the Dangal. Try again, %s!\n", name);
    }
    printf("=========================================\n");

    return 0;
}