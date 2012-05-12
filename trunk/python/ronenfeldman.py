# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:30:26 2012

@author: anung
"""

import networkx as nx


def main():
    G = nx.Graph()
    G.add_edge("Mohamed Atta", "Khalid Al-Midhar")
    G.add_edge("Mohamed Atta", "Marwan Al-Sher")
    G.add_edge("Mohamed Atta", "Majed Moqed")
    G.add_edge("Mohamed Atta", "Salem Alhamzi")
    G.add_edge("Mohamed Atta", "Abdulaziz Aloma")
    G.add_edge("Mohamed Atta", "Ziad Jarrahi")
    G.add_edge("Mohamed Atta", "Satam Al Suqan")
    G.add_edge("Mohamed Atta", "Waleed M. Alshe")
    G.add_edge("Mohamed Atta", "Wail Alshehri")
    G.add_edge("Mohamed Atta", "Fayez Ahmed")
    G.add_edge("Khalid Al-Midhar", "Marwan Al-Sher")
    G.add_edge("Marwan Al-Sher", "Majed Moqed")
    G.add_edge("Majed Moqed", "Salem Alhamzi")
    G.add_edge("Salem Alhamzi", "Abdulaziz Aloma")
    G.add_edge("Abdulaziz Aloma", "Ziad Jarrahi")
    G.add_edge("Ziad Jarrahi", "Satam Al Suqan")
    G.add_edge("Satam Al Suqan", "Waleed M. Alshe")
    G.add_edge("Waleed M. Alshe", "Wail Alshehri")
    G.add_edge("Wail Alshehri", "Fayez Ahmed")
    G.add_edge("Khalid Al-Midhar", "Nawaq Alhamzi")
    G.add_edge("Khalid Al-Midhar", "Hani Hanjour")
    G.add_edge("Majed Moqed", "Nawaq Alhamzi")
    G.add_edge("Majed Moqed", "Hani Hanjour")
    G.add_edge("Majed Moqed", "Ahmed Alghamdi")
    G.add_edge("Salem Alhamzi", "Nawaq Alhamzi")
    G.add_edge("Salem Alhamzi", "Hani Hanjour")
    G.add_edge("Salem Alhamzi", "Ahmed Alghamdi")
    G.add_edge("Abdulaziz Aloma", "Hani Hanjour")
    G.add_edge("Abdulaziz Aloma", "Ahmed Algamdi")
    G.add_edge("Ziad Jarrahi", "Mohald Alshehri")
    G.add_edge("Fayez Ahmed", "Mohald Alshehri")
    G.add_edge("Nawaq Alhamzi", "Hani Hanjour")
    G.add_edge("Hani Hanjour", "Ahmed Alghamdi")
    G.add_edge("Ahmed Alghamdi", "Hamza Alghamdi")
    G.add_edge("Mohald Alshehri", "Hamza Alghamdi")
    G.add_edge("Hamza Alghamdi", "Saeed Alghamdi")
    G.add_edge("Saeed Alghamdi", "Ahmed Alnami")
    G.add_edge("Saeed Alghamdi", "Ahmed Alhaznawi")
    nx.write_graphml(G, "ronen-feldman.graphml")
    nx.write_pajek(G, "ronen-feldman.pajek.net")
    
    return G
    
    
if __name__ == '__main__':
    main()
    