import argparse

from .utils.config import load_config, save_config


def train(config):
    from .gym import Gym
    gym = Gym(config)
    gym.train()



def main():
    config = load_config()
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        title="Commends",
        dest="command",
        required=True,
    )

    # train command
    train_parser = subparsers.add_parser("train", help="train a model")
    train_parser.add_argument(
        "--name",
        help="experiment name.",
        type=str,
    )
    train_parser.add_argument(
        "--dataset",
        help="dataset that will be used in training",
        type=str,
        choices=config.get("datasets").keys(),
        required=True,
    )
    train_parser.set_defaults(func=train)

    # explain command
    # explain_parser = subparsers.add_parser(
    #    "explain",
    #    help="explain a model",
    #    epilog='the "explain" command is not yer implemented',
    # )
    # explain_parser.set_defaults(func=explain)

    args = parser.parse_args()
    config["args"] = args

    save_config(config)

    args.func(config)

if __name__ == "__main__":
    main()
