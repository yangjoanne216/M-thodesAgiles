# [Agilite]-TPJU-<Princesse>-<NGUYEN_YANG>

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
![image](https://github.com/user-attachments/assets/00e8f57c-ea39-48ae-ba8c-5391ef7e5004)
![image](https://github.com/user-attachments/assets/81c96f2d-8ddd-47b2-8bea-61b15d650610)

=> Un rectangle rouge s’affiche, indiquant que notre instance a été créée avec succès

On va essayer d’éditer le code pour modifier les comportements et les caractéristiques de cette classe. On fait un clic droit sur la classe et on sélectionne "Open Editor", ou on double-clique simplement sur la classe :

![image](https://github.com/user-attachments/assets/8a5a0936-5644-4715-9f52-c09a07968602)


Une fenêtre s’ouvre. On modifie le code à l’intérieur comme suit :
_Constructeur : C’est une méthode spéciale qui initialise un objet lorsqu’il est créé.
Attribut : C’est une variable qui représente une propriété d’un objet.
Méthode : C’est une fonction définie dans une classe qui décrit un comportement des objets._

![image](https://github.com/user-attachments/assets/89273799-5e5a-4682-b3e9-776e08f6fc74)

On recompile la classe. Lors de la recompilation, toutes les instances existantes sont supprimées (le rectangle rouge disparaît).
On crée à nouveau une instance de cette classe : 

![image](https://github.com/user-attachments/assets/93e5ffa4-b3d8-4d97-b9c8-b9e49bc2dfff)

=> Après la création d’une instance de la classe, le constructeur est appelé, donc l’instruction System.out.println s’exécute, ce qui explique l’affichage de cette fenêtre. 

![image](https://github.com/user-attachments/assets/b73cc143-755c-491c-be0b-0f40d9e0f74b)

On voit clairement qu’une instance a été créée.

![image](https://github.com/user-attachments/assets/30c6bfc5-6545-4be4-a0de-dd87696b43bb)

Maintenant, on essaie de créer des tests pour cette classe. Pour cela, on crée une nouvelle classe :
_Un test unitaire est un test qui vérifie automatiquement qu’une petite partie du code fonctionne correctement._ 

![image](https://github.com/user-attachments/assets/e1d0915f-6878-4ebb-ae9f-6e963508c5c8)
![image](https://github.com/user-attachments/assets/86e9b888-bffc-406f-a29b-938e22017d1e)

On essaie d’ouvrir le contenu de cette classe :
![image](https://github.com/user-attachments/assets/d9787ba5-48fe-4dcb-966f-1126415b0f1b)

Maintenant, on crée une méthode de teste, pour tester la méthode « foundPrinceAndBeHappyForever »:

![image](https://github.com/user-attachments/assets/42801bd0-40ff-4cf8-bbce-f7c2efa87d99)
![image](https://github.com/user-attachments/assets/1d9d73fd-96e3-4264-81e2-57cc25de1385)
![image](https://github.com/user-attachments/assets/f532fc8f-ac36-4e86-82a6-caaccf656bfb)

Les nouveaux boutons s’affichent. On crée à nouveau un objet de « Princess ». D’après, on fait comme suit :

![image](https://github.com/user-attachments/assets/69ea4a5f-f548-466b-89fe-b0b4a98986ff)

La méthode doit renvoyer « true » après avoir été appelée, on renseigne donc « true » dans ce champ:

![image](https://github.com/user-attachments/assets/1e58f653-3485-41fc-b529-ba6fbac583b7)
![image](https://github.com/user-attachments/assets/a8df9213-f73a-4cba-8da8-525ebcf929fe)

On tape « End » pour finir d’enregister la méthode de teste :

![image](https://github.com/user-attachments/assets/bed2bf12-6860-4bee-b2c4-78b94f9ae537)

On ouvre à nouveau le contenu de la classe de test. On voit qu’une nouvelle méthode a été ajoutée :

![image](https://github.com/user-attachments/assets/c199b033-479e-413b-a877-0f15a3195497)

On essaie de lancer le test :

![image](https://github.com/user-attachments/assets/51f10d1b-6f0c-457c-9134-4f7814e6bd42)
![image](https://github.com/user-attachments/assets/83781d6b-e75b-4eaf-ba5c-463f95617326)

Maintenant, on essaie de créer une autre classe « Prince » : 

![image](https://github.com/user-attachments/assets/bcdff02e-fc2e-4e84-87ed-6a7f03725184)
 
On va créer une instance de la classe : 

![image](https://github.com/user-attachments/assets/a6fb4b3c-c75c-4932-bbd9-f77cf040e135)
![image](https://github.com/user-attachments/assets/a3a0cd0a-d2de-4254-a342-7ecfdebdc0ad)

Actuellement, on constate qu’avant chaque test, il faut créer manuellement les deux instances. Il serait donc judicieux de les configurer une seule fois dans une méthode de setup, afin de les rendre disponibles pour tous les tests.
Pour faire ça, on fait comme suite :

![image](https://github.com/user-attachments/assets/409f19d1-c09f-4208-9042-8bf8d645a376)

De nouveaux morceaux de code sont ajoutés dans la classe de test :

![image](https://github.com/user-attachments/assets/07edca13-3fec-4169-8ca5-0abec7fd3705)

Maintenant, on va créer un test pour vérifier la méthode « savePrincess » de la classe Prince. Le processus est exactement le même que précédemment :

![image](https://github.com/user-attachments/assets/3974d0df-80c4-4fcf-a4d7-62f75f4aea9e)
![image](https://github.com/user-attachments/assets/dc30a0e8-4ad2-4a2e-9dfa-1661cf4e9730)
![image](https://github.com/user-attachments/assets/88f31289-a38b-488d-86d7-b826d002e699)
![image](https://github.com/user-attachments/assets/aa81deae-d1b0-4866-a597-147e77e10bea)
![image](https://github.com/user-attachments/assets/20774045-89a0-401a-8cc6-a48c2ea373bb)

 
On voit bien que la nouvelle méthode de test utilise les deux instances déjà créées dans la classe de test :

![image](https://github.com/user-attachments/assets/9c67fd86-d2f0-4d41-b3f2-3fbf63723ca5)
![image](https://github.com/user-attachments/assets/8e4b5e8d-1995-4659-8929-79ffd37aebc0)
