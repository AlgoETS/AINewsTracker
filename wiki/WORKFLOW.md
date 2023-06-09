# Flux de travail
L'apport de modifications au code du répertoire se doit de suivre certaines étapes.

## 1. Création de tâche
La première étape est de créer une nouvelle tâche décrivant les changements à apporter. Cette tâche doit suivre l'une des templates pré-configurées.
Lorsque le code est prêt à entamer lors du sprint courant, son statut devrait passer de 'Backlog' à 'À faire'.

## 2. Création de branche

Une branche doit être créée afin de pousser le nouveau code. Plusieurs types de branches peuvent être créées.

- hotfix/[description-du-bogue] : Cette branche découle d'une branche de type 'release' et doit être refusionnée avec cette même branche. Elle est utilisée pour appliquer une résolution de bogue urgente.
- release/[identifiant-unique] : Ce type de branche découle de la branche 'main'. Le nom doit comporter un identifiant unique approprié associé à la 'release'. Cet identifiant suit le motif '#.#.#a' . Une branche de release est utilisée pour un déploiement officiel.
- feature/[description-de-fonctionnalité] : Cette branche devrait découler et être refusionnée avec la branche 'develop'. Ce type de branche sert à apporter des modifications au code existant.


En plus de ces branches, dexu branches existent en permanence dans le répertoire.
- develop: Cette branche sert à ajouter de nouvelles fonctionalités au code avant de les déployer.
- main: Cette branche contient une version complètement fonctionnelle et testée du code.

Une fois la branche créée, la tâche doit être placée du statut 'Backlog' au statut 'En cours'.

## 3. Ajout de code

Le code ajouté doit être accompagné de messages de 'commit' descriptifs du changement apporté.

## 4. Fermeture de la tâche

Une fois le code développé, une 'pull request' doit être ouverte suivant la 'template' ajoutée au répertoire git. Le code doit être revu et approuvé par au moins un autre membre de l'équipe.
La tâche doit également être rattachée à la 'pull request'. Lors de la revue, le statut de cette tâche devrait être 'en revue'.

Une fois la 'pull request' fermée, le statut de la tâche devrait être mis à 'Terminé'.
