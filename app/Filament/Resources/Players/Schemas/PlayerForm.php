<?php

namespace App\Filament\Resources\Players\Schemas;

use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Schemas\Schema;

class PlayerForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema
            ->components([
                Select::make('team_id')
                    ->relationship('team', 'name')
                    ->required(),
                TextInput::make('name')
                    ->required(),
                TextInput::make('tag')
                    ->required(),
            ]);
    }
}
