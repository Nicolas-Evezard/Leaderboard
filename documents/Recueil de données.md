## Utilisateurs
| Nom                  | Description                                        | Type       | Commentaire                                         | Format         | Source de la donnée  | Fréquence de mise à jour | Entité      |
|----------------------|----------------------------------------------------|------------|-----------------------------------------------------|----------------|----------------------|--------------------------|-------------|
| Nom                  | Nom de l'utilisateur                               | Texte      | Nom de famille de l'utilisateur                     | Texte          | Application          | À chaque modification    | Utilisateur |
| Prénom               | Prénom de l'utilisateur                            | Texte      | Prénom de l'utilisateur                             | Texte          | Application          | À chaque modification    | Utilisateur |
| Date de naissance    | Date de naissance de l'utilisateur                 | Date       | Date de naissance de l'utilisateur                  | Date           | Application          | À chaque modification    | Utilisateur |
| Photo de profil      | URL de la photo de profil de l'utilisateur         | Texte      | URL de l'image de profil                            | URL            | Application          | À chaque modification    | Utilisateur |
| Mot de passe         | Mot de passe de l'utilisateur                      | Texte      | Stocké de manière sécurisée                         | Haché          | Application          | À chaque modification    | Utilisateur |
| Pseudonyme           | Pseudonyme choisi par l'utilisateur                | Texte      | Identifiant unique pour l'utilisateur               | Texte          | Application          | À chaque modification    | Utilisateur |
| Email                | Adresse email de l'utilisateur                     | Texte      | Utilisé pour la communication et authentification   | Email          | Application          | À chaque modification    | Utilisateur |
| Niveau               | Niveau d'expérience de l'utilisateur               | Nombre     | Niveau                                              | Nombre         | Application          | À chaque modification    | Utilisateur |
| Monnaie              | Monnaie virtuelle de l'utilisateur                 | Nombre     | Monnaie virtuelle de l'utilisateur                  | Nombre         | Application          | À chaque modification    | Utilisateur |

## Paramètres
| Nom                  | Description                                        | Type       | Commentaire                                         | Format         | Source de la donnée  | Fréquence de mise à jour | Entité      |
|----------------------|----------------------------------------------------|------------|-----------------------------------------------------|----------------|----------------------|--------------------------|-------------|
| Utilisateur          | Référence à l'utilisateur                          | Référence  | Référence à l'utilisateur                           | Référence      | Application          | À chaque modification    | Paramètres  |
| Langue               | Langue préférée de l'utilisateur                   | Texte      | Langue préférée de l'utilisateur                    | Texte          | Application          | À chaque modification    | Paramètres  |
| Thème                | Thème préféré de l'utilisateur                     | Texte      | Thème préféré de l'utilisateur                      | Texte          | Application          | À chaque modification    | Paramètres  |
| Notifications        | Préférences de notifications de l'utilisateur      | Booléen    | Activer ou désactiver les notifications             | Booléen        | Application          | À chaque modification    | Paramètres  |
| Son                  | Préférences de son de l'utilisateur                | Booléen    | Activer ou désactiver le son                        | Booléen        | Application          | À chaque modification    | Paramètres  |
| Musique              | Préférences de musique de l'utilisateur            | Booléen    | Activer ou désactiver la musique                    | Booléen        | Application          | À chaque modification    | Paramètres  |

## Amis
| Nom                  | Description                                        | Type       | Commentaire                                         | Format         | Source de la donnée  | Fréquence de mise à jour | Entité      |
|----------------------|----------------------------------------------------|------------|-----------------------------------------------------|----------------|----------------------|--------------------------|-------------|
| ID de l'ami          | Identifiant unique de l'ami                        | Texte      | Identifiant généré automatiquement                  | Texte          | Application          | À chaque ajout           | Amis        |
| Utilisateur          | Référence à l'utilisateur                          | Référence  | Référence à l'utilisateur                           | Référence      | Application          | À chaque ajout           | Amis        |
| Ami                  | Référence à l'ami                                  | Référence  | Référence à l'ami                                   | Référence      | Application          | À chaque ajout           | Amis        |
| Date d'ajout         | Date d'ajout de l'ami                              | Date       |                                                     |                |                      |                          |             |
| Statut               | Statut de l'ami (en attente, accepté, refusé)      | Texte      | Statut actuel                                       | Texte          | Application          | À chaque modification    | Amis        |
| Commentaires         | Commentaires échangés entre l'utilisateur et l'ami | Texte      |                                                     |                |                      |                          |             |
| Bloqué               | Utilisateur bloqué par l'ami                       | Booléen    | Utilisateur bloqué par l'ami                        | Booléen        | Application          | À chaque modification    | Amis        |
| Supprimé             | Utilisateur supprimé par l'ami                     | Booléen    |                                                     |                |                      |                          |             |
| Notifications        | Notifications envoyées par l'ami                   | Booléen    | Notifications envoyées par l'ami                    | Booléen        | Application          | À chaque modification    | Amis        |
| Son                  | Préférences de son de l'ami                        | Booléen    |                                                     |                |                      |                          |             | 
| Musique              | Préférences de musique de l'ami                    | Booléen    |                                                     |                |                      |                          |             |

## Achats 
| Nom                  | Description                                        | Type       | Commentaire                                         | Format         | Source de la donnée  | Fréquence de mise à jour | Entité      |
|----------------------|----------------------------------------------------|------------|-----------------------------------------------------|----------------|----------------------|--------------------------|-------------|
| ID de l'achat        | Identifiant unique de l'achat                      | Texte      | Identifiant généré automatiquement                  | Texte          | Application          | À chaque achat           | Achat       |
| Utilisateur          | Référence à l'utilisateur                          | Référence  | Référence à l'utilisateur                           | Référence      | Application          | À chaque achat           | Achat       |
| Type d'achat         | Type de l'achat effectué                           | Texte      | Skin, icône, thème, etc.                            | Texte          | Application          | À chaque achat           | Achat       |
| Montant              | Montant payé pour l'achat                          | Nombre     | Montant en monnaie                                  | Nombre         | Application          | À chaque achat           | Achat       |
| Date de l'achat      | Date à laquelle l'achat a eu lieu                  | Date       | Date de l'achat                                     | Date           | Application          | À chaque achat           | Achat       |
| Statut               | Statut de l'achat (complété, annulé, en attente)   | Texte      | Statut actuel                                       | Texte          | Application          | À chaque achat           | Achat       |


## Statistique
| Nom                    | Description                                                                      | Type       | Commentaire                                     | Format         | Source de la donnée  | Fréquence de mise à jour | Entité      |
|------------------------|----------------------------------------------------------------------------------|------------|-------------------------------------------------|----------------|----------------------|--------------------------|-------------|
| Utilisateur            | Référence à l'utilisateur                                                        | Référence  | Référence à l'utilisateur                       | Référence      | Application          | À chaque modification    | Statistique |
Nombre de parties jouées | Nombre de parties jouées par l'utilisateur                                   
Nombre de victoires      | Nombre de victoires de l'utilisateur                                            
Nombre de défaites       | Nombre de défaites de l'utilisateur                                           
Nombre de buts marqués   | Nombre de buts marqués par l'utilisateur                                       
Nombre de buts encaissés | Nombre de buts encaissés par l'utilisateur                                    
Nombre de parties jouées en équipe | Nombre de parties jouées en équipe
Nombre de parties jouées en solo | Nombre de parties jouées en solo
Nombre de parties jouées en tournoi | Nombre de parties jouées en tournoi
Nombre de parties jouées en mode facile | Nombre de parties jouées en mode facile
Nombre de parties jouées en mode difficile | Nombre de parties jouées en mode difficile
Nombre de parties jouées en mode chrono | Nombre de parties jouées en mode chrono
Nombre de parties jouées en mode points | Nombre de parties jouées en mode points
Nombre de parties jouées en mode hard | Nombre de parties jouées en mode hard
Nombre de parties jouées en mode easy | Nombre de parties jouées en mode easy
Nombre de parties jouées en mode personnalisé | Nombre de parties jouées en mode personnalisé


## Badges
| Nom                  | Description                                        | Type       | Commentaire                                     | Format         | Source de la donnée  | Fréquence de mise à jour | Entité      |
|----------------------|----------------------------------------------------|------------|-------------------------------------------------|----------------|----------------------|--------------------------|-------------|
| ID du badge          | Identifiant unique du badge                        | Texte      | Identifiant généré automatiquement              | Texte          | Application          | À chaque création        | Badge       |
| Nom du badge         | Nom du badge                                       | Texte      | Nom du badge                                    | Texte          | Application          | À chaque création        | Badge       |
| Description          | Description du badge                               | Texte      | Description du badge                            | Texte          | Application          | À chaque création        | Badge       |
| Image                | URL de l'image du badge                            | Texte      | URL de l'image du badge                         | URL            | Application          | À chaque création        | Badge       |
| Utilisateur          | Référence à l'utilisateur                          | Référence  | Référence à l'utilisateur                       | Référence      | Application          | À chaque modification    | Badge       |

## Liaison Utilisateur/Organisation
| Nom                  | Description                                        | Type       | Commentaire                                     | Format         | Source de la donnée  | Fréquence de mise à jour | Entité                   |
|----------------------|----------------------------------------------------|------------|-------------------------------------------------|----------------|----------------------|--------------------------|--------------------------|
| Utilisateur          | Référence à l'utilisateur                          | Référence  | Référence à l'utilisateur                       | Référence      | Application          | À chaque modification    | Utilisateur              |
| Organisation         | Référence à l'organisation                         | Référence  | Référence à l'organisation                      | Référence      | Application          | À chaque modification    | Organisation             |
| Rôles                | Rôle de l'utilisateur dans l'organisation          | Texte      | Rôles de l'utilisateur dans l'organisation      | Texte          | Application          | À chaque modification    | Utilisateur/Organisation |

## Liaison Utilisateur/Equipe
| Nom                  | Description                                        | Type       | Commentaire                                     | Format         | Source de la donnée  | Fréquence de mise à jour | Entité                   |
|----------------------|----------------------------------------------------|------------|-------------------------------------------------|----------------|----------------------|--------------------------|--------------------------|
| Utilisateur          | Référence à l'utilisateur                          | Référence  | Référence à l'utilisateur                       | Référence      | Application          | À chaque modification    | Utilisateur              |
| Équipe               | Référence à l'équipe                               | Référence  | Référence à l'équipe                            | Référence      | Application          | À chaque modification    | Équipe                   |
| Position             | Position de l'utilisateur dans l'équipe            | Texte      | Attaquant / Défenseur                           | Texte          | Application          | À chaque modification    | Utilisateur/Équipe       |

## Equipe
| Nom                  | Description                                        | Type       | Commentaire                                     | Format         | Source de la donnée  | Fréquence de mise à jour | Entité      |
|----------------------|----------------------------------------------------|------------|-------------------------------------------------|----------------|----------------------|--------------------------|-------------|
| Nom de l'équipe      | Nom de l'équipe créée                              | Texte      | Nom de l'équipe                                 | Texte          | Création Équipe      | À chaque modification    | Équipe      |
| Logo                 | URL du logo de l'équipe                            | Texte      | URL de l'image du logo de l'équipe              | URL            | Création Équipe      | À chaque modification    | Équipe      |
| Description          | Description de l'équipe                            | Texte      | Description de l'équipe                         | Texte          | Création Équipe      | À chaque modification    | Équipe      |


## Organisation
| Nom                  | Description                                        | Type       | Commentaire                                     | Format          | Source de la donnée   | Fréquence de mise à jour | Entité       |
|----------------------|----------------------------------------------------|------------|-------------------------------------------------|-----------------|-----------------------|--------------------------|--------------|
| Nom de l'organisation| Nom de l'organisation créée                        | Texte      | Nom de l'organisation                           | Texte           | Création Organisation | À chaque modification    | Organisation |
| Administrateur(s)    | Liste des administrateurs de l'organisation        | Texte      | Références aux utilisateurs administrateurs     | Liste de Textes | Création Organisation | À chaque modification    | Organisation |
| Joueurs              | Liste des joueurs appartenant à l'organisation     | Liste      | Références aux utilisateurs                     | Liste de Textes | Création Organisation | À chaque modification    | Organisation |
| Paramètres           | Paramètres spécifiques de l'organisation           | Texte      | Paramètres configurables                        | Texte           | Création Organisation | À chaque modification    | Organisation |
| Logo                 | URL du logo de l'organisation                      | Texte      | URL de l'image du logo de l'organisation        | URL             | Création Organisation | À chaque modification    | Organisation |

## Parties
| Nom                  | Description                                          | Type        | Commentaire                                     | Format         | Source de la donnée  | Fréquence de mise à jour | Entité      |
|----------------------|------------------------------------------------------|-------------|-------------------------------------------------|----------------|----------------------|--------------------------|-------------|
| ID de la partie      | Identifiant unique de la partie                      | Texte       | Identifiant généré automatiquement              | Texte          | Application          | À chaque création        | Partie      |
| Équipe A             | Équipe A impliquée dans la partie                    | Référence   | Référence à l'équipe                            | Référence      | Application          | À chaque modification    | Partie      |
| Équipe B             | Équipe B impliquée dans la partie                    | Référence   | Référence à l'équipe                            | Référence      | Application          | À chaque modification    | Partie      |
| Nombre de joueurs    | Nombre de joueurs dans la partie                     | Nombre      | 2, 3 ou 4 joueurs                               | Nombre         | Application          | À chaque création        | Partie      |
| Durée                | Durée de la partie en minutes                        | Nombre      | Durée totale de la partie                       | Nombre         | Application          | À chaque création        | Partie      |
| Mode de jeu          | Mode de jeu choisi pour la partie                    | Texte       | Chrono, points, hard, easy, personnalisé        | Texte          | Application          | À chaque création        | Partie      |
| Score final          | Score final de la partie                             | Référence   | Référence au score                              | Référence      | Application          | À chaque fin de partie   | Partie      |
| Règles du jeu        | Règles spécifiques appliquées à la partie            | Texte       | Règles définies pour la partie                  | Texte          | Application          | À chaque création        | Partie      |
| État de la partie    | État actuel de la partie (en cours, terminé, annulé) | Texte       | Statut de la partie                             | Texte          | Application          | À chaque modification    | Partie      |

## Score
| Nom                  | Description                                        | Type       | Commentaire                                     | Format         | Source de la donnée  | Fréquence de mise à jour | Entité      |
|----------------------|----------------------------------------------------|------------|-------------------------------------------------|----------------|----------------------|--------------------------|-------------|
| ID du score          | Identifiant unique du score                        | Texte       | Identifiant généré automatiquement             | Texte          | Application          | À chaque création        | Score       |
| Score de l'équipe A  | Score de l'équipe A dans une partie                | Nombre      | Score attribué à l'équipe A                    | Nombre         | Application          | En temps réel            | Score       |
| Score de l'équipe B  | Score de l'équipe B dans une partie                | Nombre      | Score attribué à l'équipe B                    | Nombre         | Application          | En temps réel            | Score       |
| Joueur en défense    | Joueur en défense dans une partie                  | Référence   | Référence à l'utilisateur                      | Référence      | Application          | À chaque partie          | Score       |
| Joueur en attaque    | Joueur en attaque dans une partie                  | Référence   | Référence à l'utilisateur                      | Référence      | Application          | À chaque partie          | Score       |
| Statut de validation | Statut de validation du score par les joueurs      | Booléen     | Validé ou non                                  | Booléen        | Application          | Après chaque partie      | Score       |

## Tournoi
| Nom                  | Description                                        | Type        | Commentaire                                     | Format              | Source de la donnée  | Fréquence de mise à jour | Entité      |
|----------------------|----------------------------------------------------|-------------|-------------------------------------------------|---------------------|----------------------|--------------------------|-------------|
| ID du tournoi        | Identifiant unique du tournoi                      | Texte       | Identifiant généré automatiquement              | Texte               | Création Tournoi     | À chaque création        | Tournoi     |
| Équipes inscrites    | Liste des équipes inscrites au tournoi             | Liste       | Références aux équipes                          | Liste de Références | Création Tournoi     | À chaque modification    | Tournoi     |
| Résultats            | Liste des résultats des matchs du tournoi          | Liste       | Références aux parties                          | Liste de Références | Création Tournoi     | À chaque fin de tournoi  | Tournoi     |
| Mode de tournoi      | Mode de tournoi choisi                             | Texte       | Hard, easy, personnalisé, etc.                  | Texte               | Création Tournoi     | À chaque création        | Tournoi     |
| Calendrier           | Dates et heures des matchs du tournoi              | Texte       | Programme des matchs                            | Texte               | Création Tournoi     | À chaque modification    | Tournoi     |
| Prix                 | Récompenses du tournoi                             | Texte       | Badges, skins, icônes                           | Texte               | Création Tournoi     | À chaque modification    | Tournoi     |

## Transaction
| Nom                    | Description                                             | Type        | Commentaire                                     | Format         | Source de la donnée  | Fréquence de mise à jour | Entité      |
|------------------------|---------------------------------------------------------|-------------|-------------------------------------------------|----------------|----------------------|--------------------------|-------------|
| ID de la transaction   | Identifiant unique de la transaction                    | Texte       | Identifiant généré automatiquement              | Texte          | Application          | À chaque transaction     | Transaction |
| Utilisateur            | Référence à l'utilisateur ayant effectué la transaction | Référence   | Référence à l'utilisateur                       | Référence      | Application          | À chaque transaction     | Transaction |
| Type de transaction    | Type de la transaction effectuée                        | Texte       | Achat de skin, icône, thème, etc.               | Texte          | Application          | À chaque transaction     | Transaction |
| Montant                | Montant payé pour la transaction                        | Nombre      | Montant en monnaie                              | Nombre         | Application          | À chaque transaction     | Transaction |
| Date de la transaction | Date à laquelle la transaction a eu lieu                | Date        | Date de l'achat                                 | Date           | Application          | À chaque transaction     | Transaction |
| Statut                 | Statut de la transaction (complété, annulé, en attente) | Texte       | Statut actuel                                   | Texte          | Application          | À chaque transaction     | Transaction |
| Paiement               | Informations de paiement                                | Texte       | Informations de paiaiment (carte, PayPal, etc.) | Texte          | Application          | À chaque transaction     | Transaction |

## Notification
| Nom                   | Description                                            | Type        | Commentaire                                     | Format         | Source de la donnée  | Fréquence de mise à jour | Entité       |
|-----------------------|--------------------------------------------------------|-------------|-------------------------------------------------|----------------|----------------------|--------------------------|--------------|
| ID de la notification | Identifiant unique de la notification                  | Texte       | Identifiant généré automatiquement              | Texte          | Application          | À chaque création        | Notification |
| Type de notification  | Type de notification envoyée                           | Texte       | Victoire improbable, défaite, etc.              | Texte          | Application          | À chaque événement       | Notification |
| Utilisateur concerné  | Référence à l'utilisateur concerné par la notification | Référence   | Référence à l'utilisateur                       | Référence      | Application          | À chaque événement       | Notification |
| Date                  | Date à laquelle la notification a été envoyée          | Date        | Date d'envoi de la notification                 | Date           | Application          | À chaque événement       | Notification |
| Contenu               | Contenu de la notification                             | Texte       | Message envoyé                                  | Texte          | Application          | À chaque événement       | Notification |
| Statut                | Statut de la notification (lu, non lu)                 | Texte       | Statut actuel                                   | Texte          | Application          | À chaque événement       | Notification |
