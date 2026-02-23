#!/usr/bin/env python3
"""
Police Management System - Command Line Interface

A system for managing police stations, crimes, investigations,
and maintaining public order.
"""

import argparse
import pickle
import os
import sys
from pathlib import Path
from typing import Any

from police import (
    Police,
    Policeman,
    Citizen,
    Crime,
    Investigation,
    Law,
    Security,
    ZoneNotFoundError,
    PolicemanNotFoundError,
)


DATA_DIR = Path("data")
DATA_FILES = {
    "police": "police.pkl",
    "applications": "applications.pkl",
    "history": "history.pkl",
    "citizens": "citizens.pkl",
    "laws": "laws.pkl",
    "security": "security.pkl",
}


class PoliceSystem:
    """Main system class managing all police operations."""

    def __init__(self) -> None:
        self.data_dir = DATA_DIR
        self.data_dir.mkdir(exist_ok=True)
        self._load_data()

    def _load_data(self) -> None:
        """Load data from pickle files or initialize defaults."""
        defaults: dict[str, Any] = {
            "police": Police(),
            "applications": [],
            "history": [],
            "laws": [
                Law(101, severity=1, desc="Minor offense"),
                Law(201, severity=3, desc="Theft"),
                Law(301, severity=5, desc="Violent crime"),
            ],
            "security": Security(),
            "citizens": [],
        }

        for key, filename in DATA_FILES.items():
            path = self.data_dir / filename
            try:
                with open(path, "rb") as f:
                    setattr(self, key, pickle.load(f))
                print(f"✓ Loaded: {filename}")
            except (FileNotFoundError, EOFError, pickle.UnpicklingError):
                setattr(self, key, defaults[key])
                print(f"⚠ Initialized: {filename}")

    def save_data(self) -> None:
        """Save all data to pickle files."""
        data_to_save = {
            "police": self.police,
            "applications": self.applications,
            "history": self.history,
            "citizens": self.citizens,
            "laws": self.laws,
            "security": self.security,
        }

        for key, obj in data_to_save.items():
            path = self.data_dir / DATA_FILES[key]
            with open(path, "wb") as f:
                pickle.dump(obj, f)
        print("✓ Data saved successfully")

    # Statement operations
    def create_statement(self, description: str, zone: str, suspect_idx: int, law_idx: int) -> None:
        """Create a new crime statement."""
        if not self.citizens:
            print("✗ No citizens registered")
            return
        if not self.laws:
            print("✗ No laws defined")
            return
        if not self.police.has_zone(zone):
            print(f"✗ Zone '{zone}' does not exist")
            return

        try:
            suspect = self.citizens[suspect_idx]
            law = self.laws[law_idx]
        except IndexError:
            print("✗ Invalid citizen or law index")
            return

        application = Crime(
            suspect=suspect,
            description=description,
            zone=zone,
            law=law
        )
        self.applications.append(application)
        self.police.add_crime_to_zone(zone, application)
        self.history.append(f"Crime report filed: {application.suspect.name} - {description}")
        print(f"✓ Crime report filed successfully")

    def delete_statement(self, index: int) -> None:
        """Delete a crime statement by index."""
        try:
            removed = self.applications.pop(index)
            self.history.append(f"Application deleted: {removed.description}")
            print(f"✓ Application deleted")
        except IndexError:
            print("✗ Invalid application index")

    def show_statements(self) -> None:
        """Display all crime statements."""
        if not self.applications:
            print("No crime reports filed")
            return
        for i, app in enumerate(self.applications):
            print(f"[{i}] {app}")

    # Citizen operations
    def add_citizen(self, name: str) -> None:
        """Add a new citizen."""
        citizen = Citizen(name=name)
        self.citizens.append(citizen)
        self.history.append(f"Citizen added: {name}")
        print(f"✓ Citizen '{name}' added")

    def delete_citizen(self, index: int) -> None:
        """Delete a citizen by index."""
        try:
            removed = self.citizens.pop(index)
            self.history.append(f"Citizen removed: {removed.name}")
            print(f"✓ Citizen removed")
        except IndexError:
            print("✗ Invalid citizen index")

    def show_citizens(self) -> None:
        """Display all citizens."""
        if not self.citizens:
            print("No citizens registered")
            return
        for i, citizen in enumerate(self.citizens):
            print(f"[{i}] {citizen}")

    # Police operations
    def hire_policeman(self, lastname: str, zone: str) -> None:
        """Hire a new policeman to a zone."""
        if not self.police.has_zone(zone):
            print(f"✗ Zone '{zone}' does not exist. Create it first.")
            return
        policeman = Policeman(lastname=lastname, zone=zone)
        self.police.hire(policeman=policeman, zone=zone)
        self.history.append(f"Policeman {lastname} hired to zone {zone}")
        print(f"✓ Officer {lastname} hired to zone {zone}")

    def fire_policeman(self, lastname: str) -> None:
        """Fire a policeman by lastname."""
        policemen = self.police.get_policemen()
        for policeman in policemen:
            if policeman.lastname == lastname:
                try:
                    self.police.fire(policeman)
                    self.history.append(f"Policeman {lastname} fired")
                    print(f"✓ Officer {lastname} fired")
                    return
                except (ZoneNotFoundError, PolicemanNotFoundError) as e:
                    print(f"✗ Error: {e}")
                    return
        print(f"✗ Policeman '{lastname}' not found")

    def add_zone(self, zone: str) -> None:
        """Add a new zone."""
        try:
            self.police.add_zone(zone)
            self.history.append(f"Zone '{zone}' created")
            print(f"✓ Zone '{zone}' created")
        except Exception as e:
            print(f"✗ Error: {e}")

    def show_policemen(self) -> None:
        """Display all policemen."""
        policemen = self.police.get_policemen()
        if not policemen:
            print("No policemen hired")
            return
        for policeman in policemen:
            print(policeman)

    def show_info(self) -> None:
        """Display detailed zone information."""
        if not self.police.zones:
            print("No zones registered")
            return

        for zone_id, data in sorted(self.police.zones.items()):
            print(f"\n{'='*40}")
            print(f"Zone: {zone_id}")
            print(f"{'='*40}")
            print(f"  Officers: {len(data['policemen'])}")
            for policeman in data["policemen"]:
                print(f"    - {policeman}")
            print(f"  Crimes: {len(data['crimes'])}")
            for crime in data["crimes"]:
                print(f"    - {crime}")
            print(f"  Security: {data['security']}")

    def relocate_policemen(self, indexes: list[int], target_zone: str) -> None:
        """Relocate policemen to a new zone."""
        if not self.police.has_zone(target_zone):
            print(f"✗ Target zone '{target_zone}' does not exist")
            return

        policemen = self.police.get_policemen()
        try:
            relocated = [policemen[i] for i in indexes]
            self.police.relocate(relocated_policemen=relocated, target_zone=target_zone)
            self.history.append(f"Policemen relocated to zone {target_zone}")
            print(f"✓ Officers relocated to zone {target_zone}")
        except IndexError:
            print("✗ Invalid policeman index")
        except (ZoneNotFoundError, PolicemanNotFoundError) as e:
            print(f"✗ Error: {e}")

    # Investigation operations
    def investigate_crimes(self) -> None:
        """Investigate all pending crimes."""
        if not self.applications:
            print("No crimes to investigate")
            return

        investigation = Investigation(self.applications)
        result = investigation.investigate()

        if result:
            crime, severity = result
            print(f"✓ Investigation result: {crime.suspect.name} is likely guilty")
            print(f"  Crime: {crime.description}, Severity: {severity}")

            # Assign to available policeman
            available_officers = [p for p in self.police.get_policemen() if not p.has_assignment]
            if available_officers:
                officer = available_officers[0]
                officer.assign_crime(result)
                print(f"  Assigned to: {officer.lastname}")
            else:
                print("  ⚠ No officers available for arrest")
        else:
            print("✗ Investigation inconclusive")

    def arrest_criminals(self) -> None:
        """Attempt to arrest assigned criminals."""
        officers = self.police.get_policemen()
        arrests = 0

        for officer in officers:
            if officer.has_assignment:
                if officer.arrest():
                    arrests += 1
                    self.history.append(f"Criminal arrested by {officer.lastname}")
                    print(f"✓ {officer.lastname} made an arrest")
                else:
                    print(f"✗ {officer.lastname} failed to arrest")

        if arrests == 0:
            print("No arrests made")

        # Recovery for all officers
        for officer in officers:
            officer.recovery()

    # History operations
    def show_history(self) -> None:
        """Display system history."""
        if not self.history:
            print("History is empty")
            return
        for entry in self.history:
            print(f"  • {entry}")

    def clear_history(self) -> None:
        """Clear system history."""
        self.history.clear()
        print("✓ History cleared")

    # Law operations
    def add_law(self, article: int, severity: int, desc: str) -> None:
        """Add a new law."""
        law = Law(article=article, severity=severity, desc=desc)
        self.laws.append(law)
        self.history.append(f"Law added: Article {article}")
        print(f"✓ Law added: Article {article} (Severity: {severity})")

    def show_laws(self) -> None:
        """Display all laws."""
        if not self.laws:
            print("No laws defined")
            return
        for i, law in enumerate(self.laws):
            print(f"[{i}] {law} - {law.desc}")


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        description="Police Management System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Statement commands
    stmt_parser = subparsers.add_parser("statement", help="Crime statement operations")
    stmt_sub = stmt_parser.add_subparsers(dest="subcommand")

    stmt_add = stmt_sub.add_parser("add", help="File a crime report")
    stmt_add.add_argument("description", help="Crime description")
    stmt_add.add_argument("zone", help="Zone where crime occurred")
    stmt_add.add_argument("suspect_idx", type=int, help="Suspect citizen index")
    stmt_add.add_argument("law_idx", type=int, help="Law index")

    stmt_del = stmt_sub.add_parser("delete", help="Delete a crime report")
    stmt_del.add_argument("index", type=int, help="Report index")

    stmt_sub.add_parser("list", help="List all crime reports")

    # Citizen commands
    cit_parser = subparsers.add_parser("citizen", help="Citizen operations")
    cit_sub = cit_parser.add_subparsers(dest="subcommand")

    cit_add = cit_sub.add_parser("add", help="Add a citizen")
    cit_add.add_argument("name", help="Citizen name")

    cit_del = cit_sub.add_parser("delete", help="Delete a citizen")
    cit_del.add_argument("index", type=int, help="Citizen index")

    cit_sub.add_parser("list", help="List all citizens")

    # Police commands
    pol_parser = subparsers.add_parser("police", help="Police operations")
    pol_sub = pol_parser.add_subparsers(dest="subcommand")

    pol_hire = pol_sub.add_parser("hire", help="Hire a policeman")
    pol_hire.add_argument("lastname", help="Officer lastname")
    pol_hire.add_argument("zone", help="Zone assignment")

    pol_fire = pol_sub.add_parser("fire", help="Fire a policeman")
    pol_fire.add_argument("lastname", help="Officer lastname")

    pol_zone = pol_sub.add_parser("add-zone", help="Add a new zone")
    pol_zone.add_argument("zone", help="Zone name")

    pol_sub.add_parser("list", help="List all officers")
    pol_sub.add_parser("info", help="Show zone information")

    pol_reloc = pol_sub.add_parser("relocate", help="Relocate officers")
    pol_reloc.add_argument("indexes", type=int, nargs="+", help="Officer indexes")
    pol_reloc.add_argument("target_zone", help="Target zone")

    # Investigation commands
    inv_parser = subparsers.add_parser("investigate", help="Investigate crimes")
    inv_parser.add_argument("--arrest", action="store_true", help="Attempt arrests after investigation")

    # History commands
    hist_parser = subparsers.add_parser("history", help="History operations")
    hist_sub = hist_parser.add_subparsers(dest="subcommand")
    hist_sub.add_parser("show", help="Show history")
    hist_sub.add_parser("clear", help="Clear history")

    # Law commands
    law_parser = subparsers.add_parser("law", help="Law operations")
    law_sub = law_parser.add_subparsers(dest="subcommand")

    law_add = law_sub.add_parser("add", help="Add a law")
    law_add.add_argument("article", type=int, help="Article number")
    law_add.add_argument("severity", type=int, help="Severity (1-5)")
    law_add.add_argument("desc", help="Description")

    law_sub.add_parser("list", help="List all laws")

    # System commands
    subparsers.add_parser("save", help="Save data and exit")
    subparsers.add_parser("exit", help="Exit the system")

    return parser


def interactive_mode(system: PoliceSystem) -> None:
    """Run the system in interactive mode."""
    print("\n" + "="*50)
    print("  POLICE MANAGEMENT SYSTEM")
    print("="*50)
    print("\nCommands: statement, citizen, police, investigate, history, law, save, exit")
    print("Use --help for command details\n")

    while True:
        try:
            user_input = input("police> ").strip()
            if not user_input:
                continue

            args = user_input.split()
            command = args[0]

            if command in ("exit", "quit", "q"):
                system.save_data()
                print("Goodbye!")
                break

            elif command == "save":
                system.save_data()

            elif command == "statement":
                if len(args) < 2:
                    print("Usage: statement <add|delete|list> [args...]")
                    continue
                subcmd = args[1]
                if subcmd == "add":
                    if len(args) < 6:
                        print("Usage: statement add <desc> <zone> <suspect_idx> <law_idx>")
                        continue
                    system.create_statement(args[2], args[3], int(args[4]), int(args[5]))
                elif subcmd == "delete":
                    if len(args) < 3:
                        print("Usage: statement delete <index>")
                        continue
                    system.delete_statement(int(args[2]))
                elif subcmd == "list":
                    system.show_statements()

            elif command == "citizen":
                if len(args) < 2:
                    print("Usage: citizen <add|delete|list> [args...]")
                    continue
                subcmd = args[1]
                if subcmd == "add":
                    if len(args) < 3:
                        print("Usage: citizen add <name>")
                        continue
                    system.add_citizen(args[2])
                elif subcmd == "delete":
                    if len(args) < 3:
                        print("Usage: citizen delete <index>")
                        continue
                    system.delete_citizen(int(args[2]))
                elif subcmd == "list":
                    system.show_citizens()

            elif command == "police":
                if len(args) < 2:
                    print("Usage: police <hire|fire|add-zone|list|info|relocate> [args...]")
                    continue
                subcmd = args[1]
                if subcmd == "hire":
                    if len(args) < 4:
                        print("Usage: police hire <lastname> <zone>")
                        continue
                    system.hire_policeman(args[2], args[3])
                elif subcmd == "fire":
                    if len(args) < 3:
                        print("Usage: police fire <lastname>")
                        continue
                    system.fire_policeman(args[2])
                elif subcmd == "add-zone":
                    if len(args) < 3:
                        print("Usage: police add-zone <zone>")
                        continue
                    system.add_zone(args[2])
                elif subcmd == "list":
                    system.show_policemen()
                elif subcmd == "info":
                    system.show_info()
                elif subcmd == "relocate":
                    if len(args) < 4:
                        print("Usage: police relocate <idx1> [idx2...] <target_zone>")
                        continue
                    # Last arg is zone, rest are indexes
                    target_zone = args[-1]
                    indexes = [int(x) for x in args[2:-1]]
                    system.relocate_policemen(indexes, target_zone)

            elif command == "investigate":
                system.investigate_crimes()
                if "--arrest" in args or "-a" in args:
                    system.arrest_criminals()

            elif command == "history":
                if len(args) < 2:
                    print("Usage: history <show|clear>")
                    continue
                subcmd = args[1]
                if subcmd == "show":
                    system.show_history()
                elif subcmd == "clear":
                    system.clear_history()

            elif command == "law":
                if len(args) < 2:
                    print("Usage: law <add|list> [args...]")
                    continue
                subcmd = args[1]
                if subcmd == "add":
                    if len(args) < 5:
                        print("Usage: law add <article> <severity> <desc>")
                        continue
                    system.add_law(int(args[2]), int(args[3]), args[4])
                elif subcmd == "list":
                    system.show_laws()

            else:
                print(f"Unknown command: {command}")
                print("Use 'exit' to quit or command --help for details")

        except KeyboardInterrupt:
            print("\nUse 'exit' or 'save' to save and quit")
        except Exception as e:
            print(f"✗ Error: {e}")


def main() -> None:
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()

    system = PoliceSystem()

    # If no command provided, run interactive mode
    if not args.command:
        interactive_mode(system)
        return

    # Command-line mode
    try:
        if args.command == "save":
            system.save_data()
        elif args.command == "exit":
            system.save_data()
            print("Goodbye!")
        elif args.command == "statement":
            if args.subcommand == "add":
                system.create_statement(
                    args.description, args.zone, args.suspect_idx, args.law_idx
                )
            elif args.subcommand == "delete":
                system.delete_statement(args.index)
            elif args.subcommand == "list":
                system.show_statements()
        elif args.command == "citizen":
            if args.subcommand == "add":
                system.add_citizen(args.name)
            elif args.subcommand == "delete":
                system.delete_citizen(args.index)
            elif args.subcommand == "list":
                system.show_citizens()
        elif args.command == "police":
            if args.subcommand == "hire":
                system.hire_policeman(args.lastname, args.zone)
            elif args.subcommand == "fire":
                system.fire_policeman(args.lastname)
            elif args.subcommand == "add-zone":
                system.add_zone(args.zone)
            elif args.subcommand == "list":
                system.show_policemen()
            elif args.subcommand == "info":
                system.show_info()
            elif args.subcommand == "relocate":
                system.relocate_policemen(args.indexes, args.target_zone)
        elif args.command == "investigate":
            system.investigate_crimes()
            if args.arrest:
                system.arrest_criminals()
        elif args.command == "history":
            if args.subcommand == "show":
                system.show_history()
            elif args.subcommand == "clear":
                system.clear_history()
        elif args.command == "law":
            if args.subcommand == "add":
                system.add_law(args.article, args.severity, args.desc)
            elif args.subcommand == "list":
                system.show_laws()

        # Auto-save after commands
        system.save_data()

    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
