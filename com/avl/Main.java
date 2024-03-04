package com.avl;

public class Main {
    public static void main(String[] args) {
        // Criando uma árvore AVL usando a classe BlackBox
        BlackBox blackBoxTree = new BlackBox();
        int[] values = {10, 20, 30, 40, 50, 25};
        System.out.println("Árvore AVL resultante (BlackBox):");
        testTree(blackBoxTree, values);

        // Criando uma árvore AVL usando a classe chatGPT
        chatGPT chatGPTTree = new chatGPT();
        System.out.println("Árvore AVL resultante (chatGPT):");
        testTree(chatGPTTree, values);
        
        // Criando uma árvore AVL usando a classe codeium
        codeium codeiumTree = new codeium();
        System.out.println("Árvore AVL resultante (codeium):");
        testTree(codeiumTree, values);
        
        // Criando uma árvore AVL usando a classe rosetta
        rosetta rosettaTree = new rosetta();
        System.out.println("Árvore AVL resultante (rosetta):");
        testTree(rosettaTree, values);
        
        // Criando uma árvore AVL usando a classe theAlgorithms
        theAlgorithms theAlgorithmsTree = new theAlgorithms();
        System.out.println("Árvore AVL resultante (theAlgorithms):");
        testTree(theAlgorithmsTree, values);
        
        // Criando uma árvore AVL usando a classe gemini
        gemini<Integer> geminiTree = new gemini<>();
        System.out.println("Árvore AVL resultante (gemini):");
        testTree(geminiTree, values);
    }

    static void testTree(BlackBox tree, int[] values) {
        for (int value : values) {
            tree.root = tree.insert(tree.root, value);
        }
        inOrder(tree.root);
        System.out.println();
    }

    static void testTree(chatGPT tree, int[] values) {
        for (int value : values) {
            tree.root = tree.insert(tree.root, value);
        }
        inOrder(tree.root);
        System.out.println();
    }
    
    static void testTree(codeium tree, int[] values) {
        for (int value : values) {
            tree.root = tree.insert(tree.root, value);
        }
        inOrder(tree.root);
        System.out.println();
    }
    
    static void testTree(rosetta tree, int[] values) {
        for (int value : values) {
            tree.insert(value);
        }
        tree.printBalance();
        System.out.println();
    }
    
    static void testTree(theAlgorithms tree, int[] values) {
        for (int value : values) {
            tree.insert(value);
        }
        tree.printBalance();
        System.out.println();
    }
    
    static void testTree(gemini<Integer> tree, int[] values) {
        for (int value : values) {
            tree.root = tree.insert(tree.root, value);
        }
        tree.inOrderTraversal(tree.root);
        System.out.println();
    }

    static void inOrder(codeium.Node node) {
        if (node != null) {
            inOrder(node.left);
            System.out.print(node.key + " ");
            inOrder(node.right);
        }
    }

    static void inOrder(com.avl.Node node) {
        if (node != null) {
            inOrder(node.left);
            System.out.print(node.key + " ");
            inOrder(node.right);
        }
    }
}
