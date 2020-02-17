import {Injectable} from '@angular/core';
import {AuthService} from "./auth.service";

@Injectable({
  providedIn: 'root'
})
export class InstructionService {
  instructions = {
    studying: {
      TC: [
        'Studying alone may much effective than group studying',
        'Explore practical ways to study where you can perform hands-on learning',
        'Focus on writing answers to questions while studying',
        'Take a short break periodically while studying for a long time',
        'Study by answering questions in the textbook and assignments',
        'Try brainstorming the content that you are planning to study',
        'Always correct the answers you have written using textbook or notes',
        'Take down short notes in point form while studying',
        'Revise your studies once in a while',
      ],
      SP: [
        'Start studying with a small plan',
        'Refer to external sources like books, papers, and internet when studying',
        'Always follow the notes and textbook in the order of syllabus',
        'Learn by making questions from the lessons and answering them by yourself',
        'Follow example questions when studying before you try answering',
        'Do not worry too much about certain theorems and how they are proved. Only the application is important',
        'Do not worry too much about neatness when studying',
        'Only focus study on the given scope of the syllabus. Do not overanalyze external sources.',
        'Practice to do questions on time',
        'Do not consume a lot of time when making a study plan',
      ]
    },
    examination: {
      TC: [
        'Properly write the complete answer assuming the examiner has no knowledge about the question',
        'Use the scrap paper for planning your answers',
        'Use all of the time allocated',
        'Organize the answer according to the asked question. Do not write all the things you know without understanding',
        'Properly label your diagrams and complete your writings properly',
        'Read the question properly. Don’t make up your own version of what you think the question means',
      ],
      SP: [
        'If you are struggling to answer a question, think of a similar question and work through like that',
        'Don’t try to provide the long descriptive answers, if you are unsure.',
        'When you are short of time, put a mark by the answers that you need to go back and check',
        'Don’t linger and think hard on the questions that you think you are unsure',
        'Don’t over analyze the directions and questions',
        'Don’t waste a lot of time answering the questions that you think you are unsure',
        'Don’t over plan content for writing',
        'Don’t worry about your mistakes. Correct them when you are double-checking your answers',
      ]
    },
    group: {
      TC: [
        'Encourage others to engage in hands-on activities',
        'Allow others to express their ideas',
        'Trust that your team members also want to do well with the task',
        'Use diagrams and sketches to explain what you are thinking',
      ],
      SP: [
        'Observe that each person has his/her own way of doing things',
        'Don’t let others think that you’re questioning their ability',
        'Allow some flexibility. You don’t always have to follow every direction step-by-step',
        'Do not expect perfect results immediately',
        'Don’t be worried too much if someone doesn’t follow the plan as thoroughly as you would like',
      ]
    }
  };

  characteristics = {
    SP: [
      'Working to a plan',
      'Follows examples',
      'Cares about neatness',
      'Explore information',
      'Cares about constant feedback',
    ],
    TC: [
      'Likes to perform hands-on activities',
      'Likes to experiments',
      'Willing to take risks',
      'Performs well independently',
    ]
  };

  constructor(private auth: AuthService) {
    this.instructions.studying['M'] = [...this.instructions.studying.SP, ...this.instructions.studying.TC];
    this.instructions.examination['M'] = [...this.instructions.examination.SP, ...this.instructions.examination.TC];
    this.instructions.group['M'] = [...this.instructions.group.SP, ...this.instructions.group.TC];
  }

  getInstruction(n) {
    // 0 - Mixed
    // 1 - Precision, Sequence
    // 2 - Technical, Confluence
    let res = {
      group: [],
      exam: [],
      study: []
    };
    if(this.auth.user){
      let ls = this.auth.user['predicted']['learningStyle'];
      ls = (ls == 0 ? 'M' : (ls == 1 ? 'SP' : 'TC'));

      res.study = this.randomPick(this.instructions.studying[ls], n);
      res.exam = this.randomPick(this.instructions.examination[ls], n);
      res.group = this.randomPick(this.instructions.group[ls], n);
    }
    console.log(this.instructions);
    return res;
  }

  randomPick(arr, n){

    let shuffle = (array) => {
      let currentIndex = array.length, temporaryValue, randomIndex;

      // While there remain elements to shuffle...
      while (0 !== currentIndex) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
      }

      return array;
    };

    shuffle(arr);
    return arr.slice(0, n)
  }
}
