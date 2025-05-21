# [Agilite]-TPJU-<Princesse>-<NGUYEN_YANG>

## Concepts de POO

Aujourd'hui, nous allons apprendre les concepts de la programmation orientée objet (POO), grâce à l'aide de l'outil BlueJ.

_Tout d'abord, nous allons vous raconter une histoire_

_Il était une fois une princesse nommée Rapunzel. Ses cheveux possédaient une magie qui permettait de rester jeune pour toujours. À cause de cela, elle fut emprisonnée pendant de nombreuses années dans un château par une sorcière._

_Elle attendait qu’un prince vienne la sauver de sa situation. Le prince Flynn, ayant entendu parler de cette histoire, décida de partir à l’aventure pour la libérer._


Tout d’abord, téléchargez BlueJ à l’adresse suivante : http://www.bluej.org/, puis installez-le sur votre machine.
Créons une première classe nommée « Princess » :

_Classe : C’est un modèle qui définit les caractéristiques et comportements communs à un ensemble d’objets._

![image](https://github.com/user-attachments/assets/90bece13-480d-4dd3-a21d-3eef1711726d)

Une boîte rectangulaire s’affiche pour représenter notre classe :
 
![image](https://github.com/user-attachments/assets/15b735db-07a9-4ba1-812d-c01642ea5f80)

On va essayer de compiler cette classe:

![image](https://github.com/user-attachments/assets/3dac0612-ed36-4834-b589-0028a44d8db6)

![image](https://github.com/user-attachments/assets/f0fa11bf-21bf-40cb-bd67-8066788d7f4f)

=> Il n’y a plus de rayures, ce qui indique que la classe a été compilée avec succès.

On va essayer de créer une instance de cette classe :
_Instance / Objet : C’est un exemplaire concret créé à partir d’une classe._
 
![image](https://github.com/user-attachments/assets/6944c2f6-4f80-4a00-a19f-6d4647a16925)

![image](https://github.com/user-attachments/assets/81c96f2d-8ddd-47b2-8bea-61b15d650610)

=> Un rectangle rouge s’affiche, indiquant que notre instance a été créée avec succès

On va essayer d’éditer le code pour modifier les comportements et les caractéristiques de cette classe. On fait un clic droit sur la classe et on sélectionne "Open Editor", ou on double-clique simplement sur la classe :

![image](https://github.com/user-attachments/assets/8a5a0936-5644-4715-9f52-c09a07968602)


Une fenêtre s’ouvre. On modifie le code à l’intérieur comme suit :
_Constructeur : C’est une méthode spéciale qui initialise un objet lorsqu’il est créé.
Attribut : C’est une variable qui représente une propriété d’un objet.
Méthode : C’est une fonction définie dans une classe qui décrit un comportement des objets._

<img width="746" alt="Screenshot 2025-05-20 at 09 27 21" src="https://github.com/user-attachments/assets/917fb8c9-47df-42ca-aef7-cb19a2853a62" />

On recompile la classe. Lors de la recompilation, toutes les instances existantes sont supprimées (le rectangle rouge disparaît).
On crée à nouveau une instance de cette classe : 

<img width="342" alt="Screenshot 2025-05-20 at 12 08 03" src="https://github.com/user-attachments/assets/e1dd8a90-bc79-45f4-aa41-ee5569cedffa" />

=> Après la création d’une instance de la classe, le constructeur est appelé, donc l’instruction System.out.println s’exécute, ce qui explique l’affichage de cette fenêtre. 

On voit clairement qu’une instance a été créée.

![image](https://github.com/user-attachments/assets/30c6bfc5-6545-4be4-a0de-dd87696b43bb)

Maintenant, on essaie de créer des tests pour cette classe. Pour cela, on crée une nouvelle classe :
_Un test unitaire est un test qui vérifie automatiquement qu’une petite partie du code fonctionne correctement._ 

<img width="315" alt="Screenshot 2025-05-20 at 09 22 29" src="https://github.com/user-attachments/assets/b54b6bc5-9bad-4a47-9260-4c460eaa9a2d" />


<img width="195" alt="Screenshot 2025-05-20 at 13 05 40" src="https://github.com/user-attachments/assets/b2c545de-a252-41ab-a6e4-541e5eefcb62" />

On essaie d’ouvrir le contenu de cette classe :

<img width="631" alt="Screenshot 2025-05-20 at 09 23 30" src="https://github.com/user-attachments/assets/fbca9b0a-2f40-4f72-b9ac-4aae709bcd2a" />

Maintenant, on crée une méthode de teste, pour tester la méthode « foundPrinceAndBeHappyForever »:

<img width="348" alt="Screenshot 2025-05-20 at 09 23 57" src="https://github.com/user-attachments/assets/a429425a-ce50-41da-b010-d8debd631b30" />

![image](https://github.com/user-attachments/assets/1d9d73fd-96e3-4264-81e2-57cc25de1385)

<img width="309" alt="Screenshot 2025-05-20 at 13 08 12" src="https://github.com/user-attachments/assets/a807127d-e65e-4f3b-a7c9-9d2440102f89" />

Les nouveaux boutons s’affichent. On crée à nouveau un objet de « Princess ». D’après, on fait comme suit :

![image](https://github.com/user-attachments/assets/69ea4a5f-f548-466b-89fe-b0b4a98986ff)

La méthode doit renvoyer « true » après avoir été appelée, on renseigne donc « true » dans ce champ:

![image](https://github.com/user-attachments/assets/1e58f653-3485-41fc-b529-ba6fbac583b7)
![image](https://github.com/user-attachments/assets/a8df9213-f73a-4cba-8da8-525ebcf929fe)

On tape « End » pour finir d’enregister la méthode de teste :

![image](https://github.com/user-attachments/assets/bed2bf12-6860-4bee-b2c4-78b94f9ae537)

On ouvre à nouveau le contenu de la classe de test. On voit qu’une nouvelle méthode a été ajoutée :

<img width="748" alt="Screenshot 2025-05-20 at 13 11 25" src="https://github.com/user-attachments/assets/ee6ad142-4e87-49c1-8712-fa0f1a843b6e" />

On essaie de lancer le test :

![image](https://github.com/user-attachments/assets/51f10d1b-6f0c-457c-9134-4f7814e6bd42)
![image](https://github.com/user-attachments/assets/83781d6b-e75b-4eaf-ba5c-463f95617326)

Maintenant, on essaie de créer une autre classe « Prince » : 
<img width="723" alt="Screenshot 2025-05-20 at 13 12 31" src="https://github.com/user-attachments/assets/7ff096f7-ee0a-43a1-864e-bc1c96f1b59d" />
 
On va créer une instance de la classe : 

<img width="362" alt="Screenshot 2025-05-20 at 13 14 07" src="https://github.com/user-attachments/assets/c6266164-a5ab-4370-b2af-2b1bcaa50aa4" />

![image](https://github.com/user-attachments/assets/a3a0cd0a-d2de-4254-a342-7ecfdebdc0ad)

Actuellement, on constate qu’avant chaque test, il faut créer manuellement les deux instances. Il serait donc judicieux de les configurer une seule fois dans une méthode de setup, afin de les rendre disponibles pour tous les tests.
Pour faire ça, on fait comme suite :

<img width="471" alt="Screenshot 2025-05-20 at 13 16 07" src="https://github.com/user-attachments/assets/b6f3c556-5314-47ed-aed6-b7b595adf186" />


De nouveaux morceaux de code sont ajoutés dans la classe de test :
<img width="764" alt="Screenshot 2025-05-20 at 10 14 05" src="https://github.com/user-attachments/assets/58e0e0f1-04f7-427f-9455-9b06e01b0dac" />

Maintenant, on va créer un test pour vérifier la méthode « savePrincess » de la classe Prince. Le processus est exactement le même que précédemment :

<img width="348" alt="Screenshot 2025-05-20 at 09 23 57" src="https://github.com/user-attachments/assets/a675cd09-6d19-42a7-af7c-9171aaf19c26" />

![image](https://github.com/user-attachments/assets/88f31289-a38b-488d-86d7-b826d002e699)

![image](https://github.com/user-attachments/assets/aa81deae-d1b0-4866-a597-147e77e10bea)

![image](https://github.com/user-attachments/assets/20774045-89a0-401a-8cc6-a48c2ea373bb)

 
On voit bien que la nouvelle méthode de test utilise les deux instances déjà créées dans la classe de test :

![image](https://github.com/user-attachments/assets/9c67fd86-d2f0-4d41-b3f2-3fbf63723ca5)
<img width="544" alt="Screenshot 2025-05-20 at 11 57 19" src="https://github.com/user-attachments/assets/e62eb5b6-3a6a-4fd4-8f16-556ae6b020f4" />


## Test
On utilise la librairie "behave" pour tester la fonctionnalité des codes. Détails des codes de test se trouvent dans le dossier "features" et détails des codes d'implémentation des 2 classes se trouvent dans le fichier "kingdom.py".

Voici les résultats de test:

![image](https://github.com/user-attachments/assets/3eb28be6-435c-4c35-af18-0990db803456)
