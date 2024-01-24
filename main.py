import os
import argparse




def train(config):
    print('the "explain" command is not yet implemented.')



def explain(config):
    print('the "explain" command is not yet implemented.')




def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='Commends',
                                       dest='command',
                                       required=True,
                                       )
    
    # train command
    train_parser = subparsers.add_parser('train', help='train a model')
    # train_parser.add_argument('architecture')
    train_parser.add_argument('--dataset',
                              help='dataset that will be used in training',
                              type=str,
                              required=True,
                              )
    train_parser.add_argument('-v',
                              '--verbose',
                              action='store_true'
                              )
    train_parser.set_defaults(func=train)
     
    
    # explain command
    explain_parser = subparsers.add_parser('explain',
                                           help='explain a model', 
                                           epilog='the "explain" command is not yer implemented')
    explain_parser.set_defaults(func=explain)
    
    



    args = parser.parse_args()
    args.func(args)




if __name__ == '__main__':
    main()
